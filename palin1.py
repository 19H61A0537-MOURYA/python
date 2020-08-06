#4.python program to check given string is palindrome or notstring=input(("Enter a string:"))
str = input("enter the string:") # initial string
reversed=[]
count=0
f=0
for i in str:
      count=count+1

while count>0: 
    reversed += str[count - 1]
    count = count - 1
for i in range(0,int(count/2)):
    if str[i]!=reversed[i]:
        f=0
    f=1
        
if (f==0):
    print("string is palindrome")
else:
    print("string isnt a palindrome")
