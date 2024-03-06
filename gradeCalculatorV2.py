def main():
    print('          GRADE CALCULATOR')
    grades = [0] * 7
    sub = ['Programming Languages', 'Information Management', 'Algorithms and Complexity',
           'Life and Works of Rizal', 'Science, Technology, and Society', 'Physical Education',
           'Networks and Communication']

    for i in range(len(sub)):
        grade = input('Enter Grade In ' + sub[i] + ': ')
        grades[i] = float(grade)

    average_grade = sum(grades) / len(sub)

    def convert_to_gwa(average_grade):
        return (
            1.00 if 99.0 <= average_grade <= 100.0 else
            1.25 if 96.0 <= average_grade <= 98.0 else
            1.5 if 93.0 <= average_grade <= 95.0 else
            1.75 if 90.0 <= average_grade <= 92.0 else
            2.0 if 87.0 <= average_grade <= 89.0 else
            2.25 if 84.0 <= average_grade <= 86.0 else
            2.5 if 81.0 <= average_grade <= 83.0 else
            2.75 if 76.0 <= average_grade <= 80.0 else
            3.0 if 75.0 <= average_grade <= 77.74 else
            5.0)

    gwa = convert_to_gwa(average_grade)
    print("Average Grade: {:.2f}".format(average_grade))
    print("Converted GWA: {:.2f}".format(gwa))
    description = "PASSED" if gwa <= 3.00 else "FAIL"
    print("DESCRIPTION: " + description)

    while True:
        choice = input("Do you want to continue (y/n)? ").lower()
        if choice == 'y':
            main()
        elif choice == 'n':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
if __name__ == "__main__":
    main()
