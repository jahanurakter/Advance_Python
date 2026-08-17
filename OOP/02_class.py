#class is a blue print of an object 
#Classes are user-defined data types that act as the blueprint 
# for individual objects, attributes and methods

class student:
    roll = ""
    gpa = ""

jeffy = student()             #jeffy akta object er  calss hocce student
jeffy.gpa= 4.5
jeffy.roll= 5

# print(jeffy.roll)
print(f"GPA={jeffy.gpa}, Roll={jeffy.roll}")


#----------------------------------------------------
class details:                      #class make 
    def set_value(self,a,b):
        self.roll=a
        self.gpa=b
    def display(self):
        print(f"Roll={self.roll},GPA={self.gpa}")

kamal=details()                 #object kamal er class Student    
kamal.set_value(5,3.8)              #function k call
kamal.display()                     #output show er jonno