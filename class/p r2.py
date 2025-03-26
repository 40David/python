def liner_reg(x,y):
    n=len(x)
    x_mean=sum(x)/n
    y_mean=sum(y)/n
    num=sum((x[i]-x_mean)*(y[i]-y_mean)for i in range(n))
    den=sum((x[i]-x_mean)**2 for i in range (n))
    slope=num/den
    intercept=y_mean-slope*x_mean
    return slope,intercept
def r_squred(x,y,slope,intercept):
    prediction=[slope*xi+intercept for xi in x]
    sstotal=sum((yi-sum(y)/len(y))**2 for yi in y)
    ssresidual=sum((yi-pred)**2 for yi,pred in zip(y,prediction))
    return 1-(ssresidual/sstotal)

x=[1,2,3,4,5]
y=[2,4,5,4,5]
slope,intercept = liner_reg(x,y)
r2=r_squred(x,y,slope,intercept)
print(f"slope:{slope},intercept{intercept}")
print(f"R2={r2:.4f}")
if r2>0.8:
    print("strong fit")
elif r2>0.5:
    print("moderate fit")
else:
    print("weak fit")
