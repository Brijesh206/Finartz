options = ("1. Surname Firstname Middlename", "2. Firstname Middlename Surname")

print("Formates for name: ")
print(options[0])
print(options[1])
optionType = int(input("How do you want to enter your name?\npress 1 for first option and 2 for second option : "))

if(optionType == 1 or optionType == 2): 
    
    fullName = input("Enter your name in your selected formate : ")

    arr = fullName.split()

    if (optionType ==1):
        slice_obj = slice(0,2)
        name = arr[slice_obj]
        print(name[0] + " " + name[1])
    elif (optionType == 2):
        slice_obj = slice(0, 3, 2)
        name = arr[slice_obj]
        print(name[0] + " " + name[1])
else:
    print("Invalid input :(")
