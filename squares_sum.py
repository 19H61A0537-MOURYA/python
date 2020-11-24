def square(x):
    x*=x
    return x
num=[]
num=list(filter(square,range(1,11)))
sum=0
for i in num:
    sum+=i
print("sum of squares from 1-10=",sum)
    
