#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni

#Class definition
class Student:
    def __init__(self,name, midScore, finalScore, projectScore):
        self.name=name
        self.midScore=midScore
        self.finalScore=finalScore
        self.projectScore=projectScore

    def get_name(self):
        return self.name

    def get_sum(self):
        return  self.sum

    def get_avg(self):
        return  self.avg

    def calculate(self):
        self.sum=self.midScore+ self.finalScore + self.projectScore
        self.avg=self.sum/3

name=input("Enter your name:")
midScore=int(input("Enter midterm grades:"))
finalScore=int(input("Enter final exam grades:"))
projectScore=int(input("Enter assignment grade:"))

#Object creation
student1=Student(name,midScore,finalScore,projectScore)
#Sum and average calculation method call
student1.calculate()

print("Student name=",student1.get_name())
print("Sum=",student1.get_sum())
print("Average=",student1.get_avg())