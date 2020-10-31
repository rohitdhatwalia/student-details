class students:
    def __init__(self):
        self.name = input("Emter your name : ")
        self.rollno = input("Enter your roll number : ")

    def marks(self):
        self.m1 = int(input("Enter your marks of python : "))
        self.m2 = int(input("Enter your marks of CN : "))
        self.m3 = int(input("Enter your marks of FLAT : "))
        self.m4 = int(input("Enter your marks of SE : "))
        self.m5 = int(input("Enter your marks of DBMS : "))

class total(students):
    def __init__(self):
        students.__init__(self)
        self.res = 0
    
    def display(self):
        self.res =  self.m1+ self.m2+ self.m3+ self.m4+ self.m5
        print("Total marks : ",self.res)

class percentage(total,students):
    def __init__(self):
        total.__init__(self)
        self.per = 0

    def result(self):
        self.per = self.res/5
        print("Percentage : ",self.per)
        
obj1 = percentage()
obj1.marks()
obj1.display()
obj1.result()