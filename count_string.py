#counting the occurences
def search(str,x):
    count=0
    for i in range(0,len(str)):
        if(x==str[i]):
            count+=1
    print("character ",x,"occured ",count," times")
print("enter the string")
str=input()
print("enter the character to be searched and counted:")
x=input()
search(str,x)
