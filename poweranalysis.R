library(lme4)
library(simr)
r_extended <- extend (r,along="id",n=100)
powerC<-powerCurve(fit=r_extended,test=fixed("ratingType"),along="id",breaks=c(0,50,100,150,200))
print(powerC)

r1 = lmer (value~ratingType+(1|id)+(1|trial)+(1|faceIdentity),dif);summary(r1)
fixef(r1)["ratingTypeEstimated Mean"]
fixef(r1)["ratingTypeEstimated Mean"]<--0.6
powerSim(r1)
r2<-extend(r1,along="trial",n=150)
powerSim(r2)

id<-unique(dif$id)
trial<-unique(dif$trial)
pow=list()
for(i in 1:50){
  print(i)
  selectiontrial<-sample(trial[trial],50)
  selectionid<-sample(id[id],20)
  dif2<-dif[which(dif$trial%in%selectiontrial&dif$id%in%selectionid),]
  fit<-lmer(value~ratingType+(1|id)+(1|trial),dif2)
  power<-powerSim(fit,nsim=20)
  pow[i]<-power[1]
}
  p<-unlist(pow)
  p=p*5
  mean(p)
  hist(p)