students = [1, 2, 3, 5, 6, 7, 8]
 
for i in range(0, len(students)):
    print(students[i])

for student in students:
    print(student)

for n in students:
    if (n % 2 == 1):
        print(n)    