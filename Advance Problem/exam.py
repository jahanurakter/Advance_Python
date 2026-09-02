studentDB = []

def add():
    s_id = input('enter id : ')
    name = input('enter name : ')
    age = input('enter age : ')

    add_student = {
        's_id' : s_id,
        'name' : name,
        'age' : age
    }

    studentDB.append(add_student)


def view():
    for x in studentDB:
        print(x)


def repless():
    search_id = input('Enter student id to replace: ')

    for x in studentDB:
        if x['s_id'] == search_id:

            x['name'] = input('Enter new name: ')
            x['age'] = input('Enter new age: ')


while True:
    print('''
        press 1 for add
        press 2 for view
        press 3 for repless student data
        press 4 for exit
        ''')
    
    enterValue = input("enter number : ")
    if enterValue == '1' :
        add()
    elif enterValue == '2' :
        view()
    elif enterValue == '3' :
        repless()
    elif enterValue == '4' :
        break