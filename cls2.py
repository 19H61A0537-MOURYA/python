class Employee:
    empcount=0
    def __init__(self):
        id=0
        name=""
        designation=""
        salary=0
        Employee.empcount+=1
    def Data(self):
        self.id=int(input("Enter Id:"))
        self.name = input("Enter Name:")
        self.designation=input("enter the designation:")
        self.salary = int(input("Enter Salary:\t"))
    def count(self):
        print("there are %d employees"%Employee.empcount)
    def showData(self):
        print("Id\t:",self.id)
        print("Name\t:", self.name)
        print("Designation\t:",self.designation)
        print("Salary\t:", self.salary)
emp=Employee()
emp.Data()
emp.count()
emp.showData()
