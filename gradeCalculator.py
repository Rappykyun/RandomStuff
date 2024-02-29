def convertToGwa(averageGrade):
    return (
        1.25 if 96.0 <= averageGrade <= 100.0 else
        1.5 if 93.0 <= averageGrade <= 95.0 else
        1.75 if 90.0 <= averageGrade <= 92.0 else
        2.0 if 87.0 <= averageGrade <= 89.0 else
        2.25 if 84.0 <= averageGrade <= 86.0 else
        2.5 if 81.0 <= averageGrade <= 83.0 else
        2.75 if 76.0 <= averageGrade <= 80.0 else
        3.0 if 75.0 <= averageGrade <= 77.74 else
        5.0)
print('          GRADE CALCULATOR')
grades = [0] * 7
sub = ['Programming Languages', 'Information Management', 'Algorithms and Complexity', 'Life and Works of Rizal', 'Science, Technology, and Society', 'Physical Education', 'Networks and Communication']
for i in range(len(sub)):
    grade = input('Enter Grade In ' + sub[i] + ': ')
    grades[i] = float(grade)
averageGrade = sum(grades) / len(sub)
gwa = convertToGwa(averageGrade)
print("Converted GWA: {:.2f}".format(gwa))
description = "PASSED" if gwa <= 3.00 else "FAIL"
print("DESCRIPTION: "+description)