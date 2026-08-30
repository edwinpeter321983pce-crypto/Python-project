name = "thein htike aung"
age = 13
dateofbirth = "16/6/2013"
address = "myanmar,thalyin"
enime = "janita"
# these are just fake personal infformations
# coming are to ask questions
# this loop must keep running ntil you stop
while True:
    choice = input("\nwhat do you want")
    if choice == "name":
        print(f"the name of the person you want is {name.title()}")
    elif choice == "age":
        print(f"the age of the person you want is{age.title()}" )  
    elif choice == "date of birth":
        print(f"the date of the birth of the person is{dateofbirth.title()}")
    elif choice == "address":
        print(f"the address of the person you want is{address.title()}")
    elif choice == "enime":
        print(f"his enime's name is {name.title()}")
        # Ask if they want to ask another queation
        cont = input("Do you wanna ask more? (yes/no):").lower()
        if cont == "no":
            print("Good bye!!!")
            break # this totally breaks out the loop and end up the program