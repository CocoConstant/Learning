# import packages
import scanpy as sc
import pandas as pd
import dynamo as dyn
import sys
from pygam import LinearGAM, s
import numpy as np
import matplotlib.cm as cm
import matplotlib as mp
from sklearn import preprocessing
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import matplotlib as mpl

print('import package no problem')

#################### 1. data pre-processing ####################
data_pathway = sys.argv[1]
image_save_path = sys.argv[2]

# read h5ad data
sc_data = sc.read_h5ad(data_pathway)
sc.pp.neighbors(sc_data, n_neighbors=10)
sc.tl.rank_genes_groups(sc_data, 'celltype', method='t-test')
sc.pl.rank_genes_groups(sc_data, n_genes=25, sharey=False)

print('read data no problem')

# defining a function to construct dataframe
def rank_genes_groups_df(adata, key='rank_genes_groups',subgroup = None):
        dd = []
        groupby = adata.uns[key]['params']['groupby']
        if subgroup != None:
            cate = subgroup
        else:
            cate = adata.obs[groupby].cat.categories
        #print(cate)
        for group in cate:
            cols = []
            # inner loop to make data frame by concatenating the columns per group
            for col in adata.uns[key].keys():
                if col != 'params':
                       cols.append(pd.DataFrame(adata.uns[key][col][str(group)], columns=[col]))
            df = pd.concat(cols,axis=1)
            df['group'] = group
            dd.append(df)
        # concatenate the individual group data frames into one long data frame
        rgg = pd.concat(dd)
        rgg['group'] = rgg['group'].astype('category')
        return rgg

# get gene list
genes_list = list(set(rank_genes_groups_df(sc_data)['names'].tolist()))

# construct matrix using dynamo
dyn.pl.kinetic_heatmap(
    sc_data,
    genes = genes_list,
    basis ='umap',
    mode = 'pseudotime',
    tkey = 'infer_age',
    gene_order_method = 'maximum',
    color_map  = 'RdBu_r',
    show_colorbar =False,
    #dist_threshold  = 3e-10,
    #spaced_num =200,
    figsize =(20,30),
    #enforce =True
)

print('dynamo no problem')

# get dynamo psedotime data and resover
cluster_data = sc_data.uns['kinetics_heatmap']
# drop na
cluster_data.dropna(axis=0, inplace=True)


#################### 2. fit data ####################

# simulating time
try_gam = list(range(100))
gene_num = cluster_data.shape[0]

print('starting fit')

gam_fit_df = pd.DataFrame(np.zeros((gene_num, 100), dtype=float), index=cluster_data.index)
for gene_name in cluster_data.index:
    y_gam = cluster_data.loc[gene_name, :].values
    gam = LinearGAM(s(0, lam=0.6, n_splines=12), fit_intercept=False).fit(try_gam, y_gam)
    axx = gam.generate_X_grid(term=0, n=100)
    yyy = gam.predict(X=axx)
    gam_fit_df.loc[gene_name, :] = yyy

gam_fit_df.to_csv(image_save_path + '/' + 'fit_df.csv')

print('fit over')

#################### 3. data visualization ####################



cmap = sns.color_palette( "ch:start=.2,rot=-.3", n_colors=1_000)
sns.set_context( context='paper')
sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'lightgrey'})


# using seaborn clustermap, which uses scipy hierarchical clustering
# this will take a while to run
ax = sns.clustermap( gam_fit_df, metric='euclidean', method='ward', col_cluster=False, row_cluster=True, cmap=cmap, figsize=(15,15), standard_scale=0)
ax.cax.set_visible(False)
num_stages = 6
ticks = np.linspace(0, gam_fit_df.shape[1], num_stages)
ax.ax_heatmap.set_xticks( ticks)
# ax.ax_heatmap.set_xticklabels( adata.uns['stage_order'], rotation=90);
ax.ax_row_dendrogram.set_visible(True)
plt.setp( ax.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
ax.ax_heatmap.set_title( "Trend Fit Clustering")
plt.savefig(image_save_path + '/' + 'Trend_Fit_Clustering.pdf', dpi=300, format='pdf')




# set colors used in manuscript
tttt = cm.get_cmap('tab20', 20)
tab20 = []
for i in range(tttt.N):
    rgba = tttt(i)
    tab20.append( mp.colors.rgb2hex(rgba))



dend_link = ax.dendrogram_row.linkage
cut_tree = hierarchy.cut_tree(dend_link, height=60).squeeze()
u_clust = np.unique(cut_tree)

devDEGs_df = pd.DataFrame()
devDEGs_df['gene_name'] = [i for i in gam_fit_df.index]
devDEGs_df['gene_trend'] = cut_tree

row_order = (hierarchy.leaves_list(dend_link))
_, idx = np.unique(cut_tree[row_order], return_index=True)
cluster_order = cut_tree[row_order][np.sort(idx)]

# format cluster colors for plotting
lut = dict( zip( cluster_order, tab20))
row_colors = pd.Series( cut_tree).map( lut)

ax = sns.clustermap( gam_fit_df.reset_index(drop=True), row_linkage=dend_link, row_colors=row_colors, col_cluster=False, 
                     row_cluster=True, cmap=cmap, figsize=(30,30), standard_scale=0, 
                     yticklabels=[], cbar_pos=None, dendrogram_ratio=(0.10,0.01))
num_stages = 6
ticks = np.linspace(0, 100, num_stages)
ax.ax_heatmap.set_xticks( ticks)
# ax.ax_heatmap.set_xticklabels( adata.uns['stage_order'], rotation=90);
ax.ax_row_dendrogram.set_visible(True)
plt.setp( ax.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
ax.ax_heatmap.set_title( "Clustered Trend Fits")
plt.savefig(image_save_path + '/' + 'Assignment_Trend_Fit_Clustering.pdf', dpi=300, format='pdf')



# genes can be list/array of ints or gene names 
def plot_tend_avg( genes, trend_df, scat_df=None, color='green', alpha=1.0):
    min_max_scaler = preprocessing.MinMaxScaler()
    plt.figure( figsize=(4.625*3,4.625)) #, facecolor='white')
    # plot trend fit
    trends = trend_df.loc[genes,:]
    norm_td = min_max_scaler.fit_transform( trends.T)
    avg_td = np.mean( norm_td, axis=1)
    plt.plot( norm_td, linewidth=1.0, alpha=0.01, color=color)
    plt.plot( avg_td, linewidth=2.5, alpha=alpha, color='black')

    num_stages = 20 # len( adata.uns['stage_order'])
    ticks = np.linspace(0, 100, num_stages)
    plt.xticks( ticks, [""]*len(ticks))
    return



mpl.rcParams.update(mpl.rcParamsDefault)
mpl.style.use('seaborn-whitegrid')
n_grid_pts = 100
# plt.rcParams['axes.facecolor'] = 'white'
for clust_itr in cluster_order:
    clust_mk = cut_tree==clust_itr
    print( clust_itr, sum(clust_mk))
    clust_genes = gam_fit_df.index[clust_mk]
    plot_tend_avg( clust_genes, gam_fit_df, alpha=0.9, color=lut[clust_itr])
    plt.title( clust_itr)
    plt.ylim(0.0,1.0)
    plt.xlim(0,n_grid_pts-1)
    plt.savefig( f"{image_save_path}/{clust_itr}_trend-plots.png", format='png', bbox_inches='tight')
ticks = np.linspace(0, n_grid_pts-1, num_stages)
plt.xticks( ticks=ticks,labels=[1,2,3,4,5,6], rotation=90)
# have to the last one to get x-labels
# plt.savefig( f"../path/out/trend-clust_height-90_{clust_itr}_trend-plots.png", format='png', bbox_inches='tight')