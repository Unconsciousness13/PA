n = int(input())
students_grades = {}

for line in range(n):
    student,grades = input().split(' ')
    if student not in students_grades:
        students_grades[student] =  []
    students_grades[student].append(float(grades))
for (student,grade) in students_grades.items():
    grades_string = ' '.join(map(lambda grad: f'{grad:.2f}', grade))
    print(f"{student} -> {grades_string} (avg: {sum(grade) / len(grade):.2f})")

