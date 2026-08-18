# file = open("demo.txt", "a")

# while True:
#     name = input('Enter name to be added: ')
#     file.write(name + '\n')
#     choice = input("Do you want to add more names? (y/n)")
#     if  choice == 'n':
#         file.close()
#     break
file = open("demo.txt", "a")

while True:
    name = input('Enter name to be added: ')
    file.write(name + '\n')
    choice = input("Do you want to add more names? (y/n)")
    if choice == 'n':
        file.close()
        break
