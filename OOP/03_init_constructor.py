#python e akta constructor __init__ 
#constructor k call korte hoy na

class student:                      #class make 
    def __init__(self,a,b):         #__init__ akta constructor - jake call korte hoy na
        self.roll=a                 #parameter er modde roll ar gpa rakha hoise
        self.gpa=b
    def display(self):
        print(f"Roll={self.roll},GPA={self.gpa}")

jeffy=student(10, 4.75)         #parameter er value k kora hoyece  and or moddei value diye dicci    
# jeffy.display()
jeffy.roll                      #roll k direct nicce ata attribute
print(jeffy.roll)
# Maya=student(8, 4.62)
# Maya.display()
