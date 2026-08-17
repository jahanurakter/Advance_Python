#class is a blue print of an object

# class student:
#     roll = ""
#     gpa = ""

# jeffy = student()
# jeffy.gpa= 4.5
# jeffy.roll= 5

# # print(jeffy.roll)
# print(f"GPA={jeffy.gpa}, Roll={jeffy.roll}")


class student:                      #class make 
    def set_value(self,a,b):
        self.roll=a
        self.gpa=b
    def display(self):
        print(f"Roll={self.roll},GPA={self.gpa}")

kamal=student()                 #object kamal er class Student    
kamal.set_value(5,3.8)              #function k call
kamal.display()                     #output show er jonno