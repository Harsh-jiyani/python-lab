 #student Grade Calculator
name = input("Enter student name: ")
marks = []

for i in range(3):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print(f"\n{name}'s Average: {average}")
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
else:
    grade = 'D'

print("Grade:", grade)
