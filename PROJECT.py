import csv

student_fields = ['student_id', 'roll', 'name', 'batch_name']
student_database = 'students.csv'


def display_menu():
    print("---------------------------------------")
    print(" Student Database Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Calculate Grade")
    print("6. Quit")

def grade():
    print("Enter marks out of 100")
    m1=int(input("Enter marks in subject 1: "))
    m2=int(input("Enter marks in subject 2: "))
    m3=int(input("Enter marks in subject 3: "))
    m4=int(input("Enter marks in subject 4: "))
    m5=int(input("Enter marks in subject 5: "))
    tmarks=m1+m2+m3+m4+m5
    per=(tmarks)/5
    if per>=90:
        print("Total marks = ",tmarks,"\nPercentage = ",per,"\n Grade = A\n Status: Pass")
    elif per>=80 and per<90:
        print("Total marks = ",tmarks,"\nPercentage = ",per,"\n Grade = B\n Status: Pass")
    elif per>=70 and per<80:
        print("Total marks = ",tmarks,"\nPercentage = ",per,"\n Grade = C\n Status: Pass")
    elif per>=60 and per<70:
        print("Total marks = ",tmarks,"\nPercentage = ",per,"\n Grade = D\n Status: Pass")
    elif per>=50 and per<60:
        print("Total marks = ",tmarks,"\nPercentage = ",per,"\n Grade = E\n Status: Pass")
    else:
        print("Total marks = ",tmarks,"\nPercentage = ",per,"\n Grade = F\n Status: Fail")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    roll = input("Enter Student id to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Student ID: ", row[0])
                    print("Roll: ", row[1])
                    print("Name: ", row[2])
                    print("Batch name: ", row[3])
                    grade()
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")


def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    roll = input("Enter student id to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Student id not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    roll = input("Enter student id to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student id ", roll, "deleted successfully")
    else:
        print("Student id not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        search_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
