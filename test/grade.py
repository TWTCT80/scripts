students = {}

shutdown = False
while shutdown == False:
    
    name = input("Enter your name: ").lower()
    grade = input("Enter grade: ")
    students[name] = grade
    print(students)
    again = input("Would you like to enter a new name? Y or N: ").lower()
    if again == "y":
        pass
    else:
        shutdown = True
        print("Goodbye!")