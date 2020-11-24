#counting the occurences
def search(str,x,y):
     for i in range(y,len(str)):
        if(x==str[i]):
            count+=1
    print("character ",x,"occured ",count," times")
print("enter the string")
str=input()
print("enter the character to be searched and counted:")
x=input()
print("enter the position from to be searched")
y=int(input())
search(str,x,y)
