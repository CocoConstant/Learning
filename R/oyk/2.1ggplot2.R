library(ggplot2)
library(gcookbook)

setwd('C:/Users/ouyangkang/Desktop/data/csv/')

data <- read.csv('vix-daily.csv')
train <- read.csv('daily.csv')

data$Date <- as.Date(data$Date)
train$Date <- as.Date(train$Date)



# 2.1 散点图
plot(mtcars$wt, mtcars$mpg)
qplot(mtcars$wt, mtcars$mpg)
# 也可以使用便捷输入
qplot(wt, mpg, data = mtcars)

# 2.2 折线图
plot(pressure$temperature, pressure$pressure,type = 'l')
# 向图形中添加数据点和另一条折线
points(pressure$temperature, pressure$pressure, col = 'purple')
lines(pressure$temperature, pressure$pressure/2, col='red')
points(pressure$temperature, pressure$pressure/2,col = 'red')
# ggplot2
qplot(pressure$temperature, pressure$pressure, geom = 'line')
qplot(temperature, pressure, data = pressure, geom = c('line','point'))


# 2.3 条形图
barplot(BOD$demand, names.arg = BOD$Time, col=c('red','skyblue','pink','yellow','green','purple'))
barplot(table(mtcars$cyl))
# ggplot2
ggplot(BOD, aes(x=Time, y=demand)) + geom_bar(stat='identity') # ggplot2 会将它视为离散值
ggplot(BOD, aes(factor(Time), demand)) + geom_bar(stat = 'identity')

# 2.4 直方图
hist(mtcars$mpg)
hist(mtcars$mpg, breaks = 10)

ggplot(data = mtcars, aes(x = mpg)) + geom_histogram(binwidth = 3)


# 2.5 箱线图
plot(ToothGrowth$supp, ToothGrowth$len)
boxplot(len ~ supp, data = ToothGrowth)
boxplot(len ~ supp + dose, data = ToothGrowth)

qplot(ToothGrowth$supp, ToothGrowth$len, geom = 'boxplot')
qplot(interaction(ToothGrowth$supp, ToothGrowth$dose), ToothGrowth$len, geom = 'boxplot')

ggplot(ToothGrowth, aes(x=interaction(supp,dose), y=len)) + geom_boxplot()
ggplot(ToothGrowth, aes(supp, len)) + geom_boxplot()


# 2.6 函数图像
curve(x^2 + x^3 -5*x + 10, from = -4, to=4)

myfun <- function(x){
  1 + exp(-x+10)
}
ggplot(data.frame(x=c(0,20)), aes(x=x)) + stat_function(fun = myfun, geom = 'line')