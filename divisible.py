#divisible by 2 or 4
div=[]
for i in range(2,22):
    if(i%2==0 or i%4==0):
        div.append(i)
print(div)
# delete even
div1=[]
for i in range(1,10):
    if(i%2!=0):
        div1.append(i)
print(div1) 
