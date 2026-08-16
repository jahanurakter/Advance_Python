sum = 0

while True:
    num = input("Enter a Number: ")
    if num == "quit":
        break

    try:            #j code e error asar somvabona ase seta k try er modde rakha
        num = int(num)
    except:         #error hole ja korbo ta except block e lekha hoy
        print("Enter a valid number please.")
        continue
    sum = sum + num
    print(sum)
