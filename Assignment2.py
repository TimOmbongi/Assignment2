# Program Name: Assignment2.py
# Course: IT3883/Section 52337
# Student Name: Tim Ombongi
# Assignment Number: Assignment 2
# Due Date: 06/19/2026
# Purpose: This program reads student grades from a file calculates each student's average and sorts the students by average grade in descending order.
# Resources: Course notes, Textbook, Pycharm.

file = open("Assignment2.txt")

students = []
# empty list to store each student's name and average grade
line = file.readline()
# splits the line into separate pieces (name + 6 grades)
while line != "":
    parts = line.split()

    name = parts[0]

    grade1 = float(parts[1])
    grade2 = float(parts[2])
    grade3 = float(parts[3])
    grade4 = float(parts[4])
    grade5 = float(parts[5])
    grade6 = float(parts[6])
    # calculate the average of all 6 grades

    average = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6) / 6

    students.append([name, average])

    line = file.readline()

file.close()

sort = True

while sort:
    sort = False

    count = 0
    while count < len(students) - 1:
        # if current student's average is less than next student's average
        if students[count][1] < students[count + 1][1]:
            temp = students[count]
            students[count] = students[count + 1]
            students[count + 1] = temp
            sort = True

        count = count + 1  # move to next student grade paring

for student in students:
    name = student[0]
    average = student[1]
    # get student name and student average
    print(name, format(average, ".2f"))
# puts name and average to 2 decimals