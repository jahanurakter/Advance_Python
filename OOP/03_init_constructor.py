class student:                      #class make 
    def __init__(self,a,b):         #__init__ akta constructor - jake call korte hoy na
        self.roll=a                 #
        self.gpa=b
    def display(self):
        print(f"Roll={self.roll},GPA={self.gpa}")

jeffy=student(10, 4.75)        
jeffy.display()
Maya=student(8, 4.62)
Maya.display()
