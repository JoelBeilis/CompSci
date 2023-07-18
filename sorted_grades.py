__name__ = 'B. Joel'
'''
sorted_grades
Friday, May 26, 2023
List stores up to 10 grades in order from highest to lowest in a list. The application  
displays a menu of options to update list.
'''
def valid_input():
    while True:
        try:
            menu = int(input("Enter an option (0-6): "))
            if 0 <= menu <=7:
                return menu
            else:
                print("Not a valid entry!")
        except ValueError:
            print("Not a valid entry!")

def empty_list(grades):
    if sum(grades) == 0:
        return True
    else:
        return False

def valid_grade():
    while True:
        try:
            grade = int(input("Enter a grade: "))
            if 0 < grade < 101:
                return grade
            else:
                print("Not a valid grade!")
        except ValueError:
            print("Not a valid grade!")

def enter_grade(grades):
    grade = valid_grade()
    index = 0
    while index < len(grades) and grades[index] > grade:
        index += 1
    grades.insert(index, grade)
    grades.pop()
    print("Grade entered successfully!")
    show_grades(grades)


def delete_grade(grades):
    grade = valid_grade()

    if grade in grades:
        index = grades.index(grade)
    else:
        index = -1

    if index <= -1:
        print("Grade not found.")
        return

    del grades[index]
    grades.append(0)
    print("Grade deleted successfully!")
    show_grades(grades)

def show_grades(grades):
    grade_str = " | ".join(map(str, grades))
    print("Grades:", grade_str)

grades = [0] * 10

while True:
    print("\nMenu:")
    print("0: Clear list")
    print("1. Enter a grade")
    print("2. Delete a grade")
    print("3. Display lowest grade")
    print("4. Display highest grade")
    print("5. Show grades")
    print("6. Quit")

    choice = valid_input()

    if choice == 0:
        grades = [0] * 10

    elif choice == 1:
        if grades[-1] != 0:
            print("List is full")
        else:
            enter_grade(grades)

    elif choice == 2:
        if empty_list(grades) == True:
            print("The list is empty there is nothing to delete!")
        else:
            delete_grade(grades)

    elif choice == 3:
        if empty_list(grades) == True:
            print("The list is currently empty!")
        else:
            for i in range(0, 9):
                if grades[i] != 0:
                    minimum = grades[i]
            print("Lowest grade:", minimum)

    elif choice == 4:
        maximum = grades[0]
        if maximum == 0:
            print("The list is currently empty!")
        else:
            print("Highest grade:", maximum)

    elif choice == 5:
        show_grades(grades)

    elif choice == 6:
        print("Thank you for using this program! :)")
        break

    else:
        print("Invalid choice. Please try again.")

