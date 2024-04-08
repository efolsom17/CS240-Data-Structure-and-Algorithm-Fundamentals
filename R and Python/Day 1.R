install.packages("ggplot2")
library(ggplot2)
y<-rpois(20,6)
x<-0:max(y)
x<-c(x,rep(0,length(y)-length(x)))
plot(x~y)
df<-data.frame(x,y)
df
ggplot(df, aes(x,y))+geom_point()+geom_smooth()
x
