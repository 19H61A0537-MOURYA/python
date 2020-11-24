#searching a character without built in functions
def search(str,x):
    for i in range(0,len(str)):
        if(x==str[i]):
            print("character ", x," is present at index",i)
        else:
            print("not found")
            break
print("enter the string")
str=input()
print("enter the character to be searched:")
x=input()
search(str,x)

