#student details
class student:
    total_marks=0
    def __init__(self):
        self.name=input("enter the name:")
        self.roll_no=int(input("enter the roll number:"))
        self.marks=[]
    def Marks(self):
        for j in range(3):
            x=int(input("enter the marks in subject %d:"%(j+1)))
            self.marks.append(x)
            student.total_marks+=x
    def disp(self):
        print(self.name," having roll number",self.roll_no,"acquired",student.total_marks,"\n")
n=int(input("How many students:"))

for i in range(0,n):
    s=student()
    s.Marks()
for i in range(0,n):
    s.disp()
