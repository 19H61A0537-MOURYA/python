import datetime
class person():
    def __init__(self, name, dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today<datetime.date(today.year, self.dob.month, self.dob.day):
            age+=1
        if age>=18:
            print(self.name, " , Congratulation! You are eligible to vote.")
        else:
            print(self.name, " , Sorry! You should be at least 18 years of age to cast your vote.")
p=person("Mourya", datetime.date(2002,7,6))
p.check()
