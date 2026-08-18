#Reading data from the file        #open er 2ta kaj file create kora ar file khola
f= open('demo.txt','w')         #f variable er modde file ta open thakbe
print(f.write("Open file where you want to"))         #file a likhbe      
f.close()               #file kaj korar por close korte hobe


#Reading data from the file 
f= open('demo.txt','a')                 #open file alreay create hoise ti a means append file e new text create korbe
print(f.write("\n Happy"))
#print (f.write(""))
f.close() 

f= open('demo.txt','r')             
print(f.read())                 #string akare ashbe
print(f.readlines())            #list akare ashbe
f.close()
