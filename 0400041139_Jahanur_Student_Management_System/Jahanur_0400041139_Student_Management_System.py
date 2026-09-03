Stu_Management=[]
def add_student():
    s_id = input("Enter your Id:")
    s_name = input("Enter your name:")
    s_age = int(input("Enter your age:"))
    s_dept = input("Enter your dept:")
    s_marks = float(input("Enter your marks:"))

    marks=0
    if 80<=marks<=100:
        print("1st Division")
    elif 60<=marks<=79:
        print("2nd Division")
    elif 40<=marks<=59:
        print("3rd Division")
    else:
        print("Fail")

    s_data={
        "s_id": s_id,
        "s_name": s_name,
        "s_age": s_age,
        "s_dept": s_dept,
        "s_marks": s_marks
    }

    Stu_Management.append(s_data)
    print("Student Add Successfully")

def view():
    for x in Stu_Management:
        print(x)

def search():
    search_id = input("Enter your Id:")
    # search_name = input("Enter yout name:")

    for x in Stu_Management:
        if x["s_id"] == search_id:
            # if x["s_name"]==search_name:
            print(x)

def delete():
    stu_id = input("Enter your id:")

    for x in Stu_Management:
        if x ["s_id"] == stu_id:
            Stu_Management.remove(x)
            print("Delete Succesfully")
        else:
            print("ID not found")

while True:
    print('''
    1.Add Student
    2.View Student
    3.Search Id Or Name
    4.Delete Record
    5.Exit
    ''')
    option = input("Enter Your Choice:")

    if option == "1":
        add_student()
    elif option == "2":
        view()
    elif option == "3":
        search()
    elif option == "4":
        delete()
    elif option == "5":
        break








    