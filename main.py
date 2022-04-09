class Student:
    # constructor
    def __init__(self,givenName,givenAge,givenGrade,givenIdCode):
        self.name = givenName
        self.age = givenAge
        self.grade = givenGrade
        self.idCode = givenIdCode

student_List = []

#  main function
def main():
    print(
        "\t\t\t-----------------------------------------------------\n"
        "\t\t\t|++++++++++[Welcome to Student-Management]++++++++++|\n"
        "\t\t\t-----------------------------------------------------\n"
    )
    print(
        "1. Add Student Data\n"
        "2. Display Student Data\n"
        "3. Update Student Data\n"
        "4. Delete Student Data\n"
        "5. Exit\n"
    )
    # To avoid error input if enter string in the selection
    selected = False
    while selected == False:
        try:
            selected = True
            # the main code
            selection = int(input("Enter your option: "))
            options(selection)
        except: 
            print("\t\t\t[!] Invalid Input!")
            print("\t\t[+] Please try agian!\n")    
     
#  The selection option function
def options(option):
    # if user choose option 1 
    if option == 1: create()
    # if user choose option 2 
    elif option == 2: display()
    # if user choose option 3 
    elif option ==3: update()
    # if user choose option 4 
    elif option ==4: delete()
    else: print("Thank you")

def question():
    quest = input("\nDo you wish to continus [y/n]: ")
    if quest[0] == "y"or quest[0] == "Y": 
        main()

# Create Function
def create():
    try:
        amount_of_Student = int(input("\n[+] Enter the amount of Student adding: "))
        for student in range(amount_of_Student):
            print("\n\tEnter Stundent Information No."+ str(student+1))
            name = input("Name : ")
            age = int(input("Age  : "))
            grade = int(input("Grade: "))
            idCode = int(input("ID   : "))

            student = Student(name,age,grade,idCode)
            student_List.append(student)
    except:
        print("[ ! ] Value Invalid input [ ! ]")
    question()

# Display Student data Function
def display():
    if student_List:
        for i in range(student_List.__len__()):
            print("\n\tStundent Information No."+ str(i+1))
            print("|Name : ",student_List[i].name)
            print("|Age  : ",student_List[i].age)
            print("|Grade: ",student_List[i].grade)
            print("|ID   : ",student_List[i].idCode)
    else: print("No data to display yet!")
    question()

# Update Function
def update():
    print("\n\tUpdate Student information\n")
    # if len(student_List)>0:
    #     idcode = int(input("Enter the Student ID: "))
    #     # could make it cleaner by creater another search Function which return the index of object in list
    #     for i in range(len(student_List)):
    #         if idcode == student_List[i].idCode:
    #             newAge = int(input(f"Enter new Age of Student {student_List[i].name}: "))
    #             newGrade = int(input(f"Enter new Grade of Student {student_List[i].name}: "))
    #             student_List[i].age = newAge
    #             student_List[i].grade = newGrade
    #             print("Student info updated!!")
    #         elif i == len(student_List) and idcode != student_List[i].idCode:
    #             print("Data not found!!")
    # else: 
    #     print("No data\n")
    idcode = int(input("Enter the Student ID: "))
    if search(idcode):
        newAge = int(input(f"Enter new Age of Student {search(idcode).name}: "))
        newGrade = int(input(f"Enter new Grade of Student {search(idcode).name}: "))
        search(idcode).age = newAge
        search(idcode).grade = newGrade
        print("Student info updated!!")
    else: print("No data found\n")
    question()

# Delete Function
def delete():
    print("\n\tRemove Student information\n")
    idcode = int(input("Enter the Student ID: "))
    item = search(idcode)
    if item: # to see it return student_List[i] or not
        student_List.remove(item) # could use pop
        print("Student info removed!!")
    else: print("No data")
    question()

# search function
def search(idcode):
    for i in range(len(student_List)):
        if idcode == student_List[i].idCode:
            return student_List[i]
            
#  calling main function code could run
if __name__ = '__main__': main()
