def liner_reg(x,y):
    n=len(x)
    x_mean=sum(x)/n
    y_mean=sum(y)/n
    num=sum((x[i]-x_mean)*(y[i]-y_mean)for i in range(n))
    den=sum((x[i]-x_mean)**2 for i in range (n))
    slope=num/den
    intercept=y_mean-slope*x_mean
    return slope,intercept
def predict(x,slope,intercept):
    return[slope* xi + intercept for xi in x]

x=[1,2,3,4,5]
y=[2,4,5,4,5]
slope,intercept = liner_reg(x,y)
print(f"slope={slope},intercept={intercept}")
prediction= predict(x,slope,intercept)
print("prediction:,[round(p,2)forp in  prediction]")
