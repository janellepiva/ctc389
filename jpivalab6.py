#Janelle Piva
#Lab 6

students = ["Janelle", "Salina", "Daniel", "Jack", "Michelle"]

for i in students:
    print(i)

print("1. Add student to list")
print("2. Modify student name")
print("3. Remove student")

choice = int(input("Choose an option: "))

if choice == 1:
    new_student = input("Enter the name of the student you want to add: ")
    students.append(new_student)

    for i in students:
        print(i)

elif choice == 2:
    print(0, students[0])
    print(1, students[1])
    print(2, students[2])
    print(3, students[3])
    print(4, students[4])

    student_index = int(input("Enter the index number of the student you want to change: "))
    new_name = input("Enter the new student name: ")
    students[student_index] = new_name

    for i in students:
        print(i)

elif choice == 3:
    print(0, students[0])
    print(1, students[1])
    print(2, students[2])
    print(3, students[3])
    print(4, students[4])
    
    student_index = int(input("Enter the index number of the student you want to remove: "))
    students.pop(student_index)

    for i in students:
        print(i)
    
