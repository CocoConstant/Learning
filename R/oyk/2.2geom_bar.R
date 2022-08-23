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

# 8.绘制百分比堆积条形图
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

# 9. 添加数据标签
# 在条形图顶端下方
ggplot(cabbage_exp, aes(interaction(Date, Cultivar), Weight)) +
  geom_bar(stat='identity') +
  geom_text(aes(label=Weight), vjust=1.5, colour='white')
# 在条形图顶端上方
ggplot(cabbage_exp, aes(interaction(Date, Cultivar), Weight)) +
  geom_bar(stat='identity') +
  geom_text(aes(label=Weight), vjust=-0.2, colour='red')

  