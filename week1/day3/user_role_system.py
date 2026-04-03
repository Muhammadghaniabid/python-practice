admin = ['Fee', 'Attendance', 'School']
teachers = ['Classes', 'Quizes', 'Exams']
students = ['classes', 'permission']

while True:
    user_type = input('Enter your type (admin/teacher/student/exit): ')

    match user_type:
        case 'exit':
            break

        case 'admin':
            action = input("view or add: ")
            match action:
                case 'view':
                    print(admin)
                case 'add':
                    item = input("What do you want to add? ")
                    admin.append(item)

        case 'teacher':
            action = input("view or add: ")
            match action:
                case 'view':
                    print(teachers)
                case 'add':
                    item = input("What do you want to add? ")
                    teachers.append(item)

        case 'student':
            action = input("view or add: ")
            match action:
                case 'view':
                    print(students)
                case 'add':
                    item = input("What do you want to add? ")
                    students.append(item)

        case _:
            print("Invalid user type")

print("Program ended")
