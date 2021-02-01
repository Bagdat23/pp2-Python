studs = {}
n = int(input("Количество студентов: "))
s = 0
for i in range(n):
    sname = input(str(i+1) + "-й студент: ")
    point = int(input("Балл: "))
    studs[sname] = point
    s += point
 
avrg = s / n
print("\nСредний балл: %.0f. Студенты с баллом выше среднего:" % avrg)
for i in studs:
    if studs[i] > avrg:
        print(i)