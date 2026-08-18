#inheritance new class make kore onno akta class theke
#inheritance e constructor use kora jabe

class person:                             #main class
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
#----------class er vitore function k method bole
    def printname(self):
        print(self.fname, self.lname)

class student(person):        #new class j main class k use korte parbe
    pass                    #pass hocce place holder person er jonno amra hold kore rekheci
a=student("Maya","Rahman")          #a hocce object jake student class e rakha hocce
a.printname()