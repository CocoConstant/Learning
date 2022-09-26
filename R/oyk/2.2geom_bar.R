library(ggplot2)
library(gcookbook) # In order to use data

# 1. Simply draw a bar chart
ggplot(BOD, aes(Time, demand)) + geom_bar(stat='identity')
# add color and frame
ggplot(BOD, aes(Time, demand)) +
  geom_bar(stat='identity', fill='lightgreen', colour='green')

# 2. Clustered bar chart
ggplot(cabbage_exp, aes(Date, Weight)) +
  geom_bar(aes(fill=Cultivar), stat='identity', position='dodge')
# it is equal with above codes
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar)) +
  geom_bar(stat='identity', position='dodge')
# delete position='dodge'
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar)) +
  geom_bar(stat='identity')
# add black frame line and palette
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar)) +
  geom_bar(position ='dodge', stat='identity', colour='black') +
  scale_fill_brewer(palette='Pastell')
# NA value
ggplot(cabbage_exp[1:5,], aes(Date, Weight, fill=Cultivar)) +
  geom_bar(position ='dodge', stat='identity', colour='black') +
  scale_fill_brewer(palette='Pastell')

# 3. Frequency bar graph
ggplot(diamonds, aes(color)) + geom_bar()
# discrete type
ggplot(diamonds, aes(carat)) + geom_bar()

# 4. color
upc <- subset(uspopchange, rank(Change)>40)
ggplot(upc, aes(Abb, Change, fill=Region)) + geom_bar(stat='identity')

ggplot(diamonds, aes(color, carat, fill=cut)) +
  geom_bar(stat='identity', position='dodge')
# renew set color
ggplot(upc, aes(reorder(Abb, Change), Change, fill=Region)) +
  geom_bar(stat='identity', colour='black') +
  scale_fill_manual(values=c("#669933", "#FFCC66")) +
  xlab("State")

# 5. add color to positive and negative respectively
csub <- subset(climate, Source=='Berkeley' & Year >= 1900)
csub$pos <- csub$Anomaly10y >=  0
ggplot(csub, aes(Year, Anomaly10y, fill=pos)) +
  geom_bar(stat='identity', position='identity')
# optimize
ggplot(csub, aes(Year, Anomaly10y, fill=pos)) +
  geom_bar(stat='identity', position='identity', colour='black', size=0.25) +
  scale_fill_manual(values=c('#CCEEFF','#FFDDDD'), guide='none')

# 6. Regulate bar width and space between inner group 
# width=0.5
ggplot(pg_mean, aes(group, weight, fill=group)) + 
  geom_bar(stat='identity', width=0.5) +
  scale_fill_manual(values=c("#FFB6C1","#FFC0CB","#FF69B4"))
# width=0.9
ggplot(pg_mean, aes(group, weight, fill=group)) + 
  geom_bar(stat='identity') +
  scale_fill_manual(values=c("#FFB6C1","#FFC0CB","#FF69B4"))
# width=1.0
ggplot(pg_mean, aes(group, weight, fill=group)) + 
  geom_bar(stat='identity', width=1.0) +
  scale_fill_manual(values=c("#FFB6C1","#FFC0CB","#FF69B4"))
# Clustered bar chart
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar)) + 
  geom_bar(stat='identity', width=0.5, position='dodge')
# improving gap between inner group 
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar)) + 
  geom_bar(stat='identity', width=0.5, position=position_dodge(0.7))

# 7. Drawing stacked bar chart
ggplot(diamonds, aes(color, carat, fill=cut)) +
  geom_bar(stat='identity')
# cabbage_exp is a table date from gcookbook
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar)) +
  geom_bar(stat='identity')
# regulate legend order
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar)) +
  geom_bar(stat='identity') +
  guides(fill=guide_legend(reverse=TRUE))
# regulate the stacked order
library(plyr) # import the library to use desc() function
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar, order=desc(Cultivar))) +
  geom_bar(stat='identity')

Sggplot(diamonds, aes(color, carat, fill=cut, order=desc(carat))) +
  geom_bar(stat='identity')
# add palette
ggplot(diamonds, aes(color, carat, fill=cut)) +
  geom_bar(stat='identity') +
  scale_fill_brewer(palette='Pastell')

# 8. Draw percent stacked graph
library(gcookbook)
library(plyr)
ce <- ddply(cabbage_exp, "Date", transform, percent_weight=Weight/sum(Weight))
ggplot(ce, aes(Date, percent_weight, fill=Cultivar)) +
  geom_bar(stat='identity')

data <- ddply(diamonds, "color", transform, percent=carat/sum(carat))
ggplot(data, aes(color, percent, fill=cut)) +
  geom_bar(stat='identity') +
  scale_fill_brewer(palette='Set2') +
  coord_flip()

# 9. add data label
# below the top of graph
ggplot(cabbage_exp, aes(interaction(Date, Cultivar), Weight)) +
  geom_bar(stat='identity') +
  geom_text(aes(label=Weight), vjust=1.5, colour='white')
# above the top of graph
ggplot(cabbage_exp, aes(interaction(Date, Cultivar), Weight)) +
  geom_bar(stat='identity') +
  geom_text(aes(label=Weight), vjust=-0.2, colour='red')
# make the limitation of y axis big
ggplot(cabbage_exp, aes(interaction(Date, Cultivar), Weight)) +
  geom_bar(stat='identity') +
  geom_text(aes(label=Weight), vjust=0.2) +
  ylim(0, max(cabbage_exp$Weight)*1.05)
# regulate the position of y axis above the top of stacked graph----y axis will automaticly regulate
ggplot(cabbage_exp, aes(interaction(Date, Cultivar), Weight, fill=interaction(Date, Cultivar))) +
  geom_bar(stat='identity') +
  theme(legend.position='none') +
  geom_text(aes(label=Weight), vjust=-0.2) +
  ylim(0, max(cabbage_exp$Weight)*1.05)

# cluster stacked grapg
ggplot(cabbage_exp, aes(Date, Weight, fill=Cultivar)) +
  geom_bar(stat='identity', position='dodge') +
  geom_text(aes(label=Weight), vjust=1.5, color='white', 
            position=position_dodge(0.9),size=3)
# 
library(plyr)
# order data based on date and sexy
ce <- arrange(cabbage_exp, Date, Cultivar)
ce <- ddply(ce, 'Date', transform, label_y=cumsum(Weight))
ggplot(ce, aes(Date, Weight, fill=Cultivar)) +
  geom_bar(stat='identity') +
  geom_text(aes(y=label_y - 1.5, label=Weight), vjust=0.5, colour='white')

# make in middle
ce <- arrange(cabbage_exp, Date, desc(Cultivar))
ce <- ddply(ce, "Date", transform, label_y=(cumsum(Weight)-0.5*Weight))
ggplot(ce, aes(x=Date,y=Weight,fill=Cultivar)) +
  geom_bar(stat='identity') +
  geom_text(aes(y=label_y,label=Weight), colour="White")

# add another information of text
ggplot(ce, aes(Date, Weight, fill=Cultivar)) +
  geom_bar(stat='identity', colour='black') +
  geom_text(aes(y=label_y, label=paste(format(Weight, nsmall=2),'kg')), size=4) +
  guides(fill=guide_legend(reverse=TRUE)) +
  scale_fill_brewer(palette='Set3')

# Cleveland point graph
tophit <- tophitters2001[1:25,]
ggplot(tophit, aes(avg, name)) + geom_point()

# optimize
ggplot(tophit, aes(avg, reorder(name, avg))) +
  geom_point(size=3) +
  theme_bw() +
  theme(axis.text.x=element_text(angle=60,hjust=1),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour = 'grey60', linetype = 'dashed'))
  
# convert x to y
ggplot(tophit,aes(reorder(name, avg), avg)) + 
  geom_point(size=3) +
  theme_bw() +
  theme(axis.text.x = element_text(angle=90,hjust=1),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour = 'grey60', linetype = 'dashed'))
# get name variable and order them based on lg and avg
nameorder <- tophit$name[order(tophit$lg, tophit$avg)]
# make name become factor and its level identical with nameorder
tophit$name <- factor(tophit$name, levels = nameorder)
ggplot(tophit, aes(avg,name)) +
  geom_segment(aes(yend=name), xend=0, colour='grey50') +
  geom_point(size=3, aes(colour=lg)) +
  scale_colour_brewer(palette='Set1',limits=c('NL','AL')) +
  theme_bw() +
  theme(panel.grid.major.y = element_blank(),
        legend.position = c(1, 0.55),
        legend.justification = c(1,0.5))

# group show
ggplot(tophit, aes(avg, name)) +
  geom_segment(aes(yend=name), xend=0, colour='grey50') +
  geom_point(size=3, aes(colour=lg)) +
  scale_colour_brewer(palette='Set1', limits=c('NL','AL'), guide='none') +
  theme_bw() +
  theme(panel.grid.major.y = element_blank()) +
  facet_grid(lg~ ., scales='free_y', space='free_y')
