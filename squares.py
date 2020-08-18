a=0
b=0
for i in range(1,101):
    n=i*i
    m=n%10
    if(m==4):
        a=a+1
    elif(m==9):
        b=b+1
print("no.s of squares ending with 4  ",a)
print("no.s ending with 9  ",b)

        
