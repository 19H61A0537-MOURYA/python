#student details
class student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def Marks(self):
        for i in range(3):
            x=int(input("enter the marks in subject %d:"%(i+1)))
            self.marks.append(x)
    def disp(self):
        print(self.name," acquired",self.marks,"\n")
s=student("mourya")
s.Marks()
s.disp()
