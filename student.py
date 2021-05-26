class Student:

    def studentData(self):
        self.name = input("Enter Student Name : ")
        self.age = int(input("Enter age : "))
        self.branch = input("Enter Branch : ").upper()
        self.year = int(input("Enter Year : "))
        self.section = input("Enter section : ").upper()
        self.cgpa = float(input("Enter cgpa : "))

    def getData(self):
        return [self.name, self.age, self.branch, self.year, self.section, self.cgpa]


student1 = Student()
student2 = Student()
student1.studentData()
student2.studentData()

print(student1.getData())
print(student2.getData())