#current amount of water in reserviour
c=199.5e85
#after first rainfall(wastage of25% of 25e8)
r=0.75*25e8
#total amount of water in reserviour
res=c+r
#15% of current amount of water from rain
res+=res*0.15
#5% from ground resource
res+=res*0.05
#15% for irrigation
res-=res*0.15
#5% evoporated
res-=res*0.05
print("current water level is",res,"cu.m")
