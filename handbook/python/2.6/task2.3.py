"""
Немного контекста: недавно начался образовательный курс по Python. Прошло несколько недель — и настало время подвести первые итоги: насколько курс усваивается учениками и нужно ли в нём что-то менять.

Вас попросили собрать статистику по успеваемости учеников на курсе.

Что нужно сделать
Вывести общие показатели учеников программы: максимальное, среднее и минимальное значение рейтинга в процентах от максимально возможного.
Округлить результаты до целого значения с помощью функции round().
Вывести лучших учеников: топ-3 лидера по рейтингу, их фамилии в порядке убывания рейтинга и заработанный процент от максимального количества баллов. Если у студентов равный рейтинг (в абсолютном значении), то они идут в порядке их ввода — кто первый указан, тот выше по рейтингу и находится. Фамилии учеников уникальны.
На основе данных сделать предварительный вывод, насколько усваивается курс:
Если среднее значение рейтинга <= 50 — курс усваивается плохо.
Если среднее значение рейтинга > 50 — курс усваивается хорошо.
Также нужно проверить правильность введённых данных и расчётов. Если есть ошибки, выводим строку «Во введённых данных ошибка»


Формат ввода
Одна строчка, в которой через пробел подаются следующие данные:


N M Q cw sw hw tw
N (num_students) — число учеников на курсе
M (num_lessons) — количество занятий в курсе
Q (max_rating) — максимальный рейтинг
cw (classwork_coefficient) — коэффициент для активности на занятии
sw (selfwork_coefficient) — коэффициент для практики
hw (homework_coefficient) — коэффициент для домашней работы
tw (testwork_coefficient) — коэффициент для контрольной работы

Далее идут фамилии учеников (N) и несколько строчек (M) с оценками ученика на занятиях в формате:


Иванов
a₁,b₁,c₁,d₁  
a₂,b₂,c₂,d₂  
a₃,b₃,c₃,d₃  
⋮  
aₘ,bₘ,cₘ,dₘ
Сидоров
...
Где aᵢ,bᵢ,cᵢ,dᵢ — это оценки за i-ое занятие:

aᵢ (classwork_grade) — оценка за активность на занятии
bᵢ (selfwork_grade) — оценка за практику на занятии
cᵢ (homework_grade) — оценка за домашнюю работу на занятии
dᵢ (testwork_grade) — оценка за контрольную работу на занятии

Если не было активности, ученик отсутствовал либо не проявил себя на занятии — значение за активность будет 0.

Формат вывода
Построчно в следующей последовательности:

Максимальный, средний и минимальный рейтинг учеников программы. Через пробел, округлённый до целого числа с помощью round.
Построчно фамилию и имя трёх лидеров рейтинга
Предварительный вывод «как усваивается курс» (хорошо или плохо).

Max Average Min (максимальный, средний и минимальный рейтинг учеников программы)
Фамилия_1 Rating_1% (top-1)
Фамилия_2 Rating_2% (top-2)
Фамилия_3 Rating_3% (top-3)
Курс усваивается хорошо/плохо

Также сделайте проверку на верность вводных данных. Если условие не выполняется, то необходимо вывести строку «В введённых данных ошибка»

N >= 3 (количество учеников больше или равно 3)

M > 0 (количество проведённых занятий 1 и больше)

cw, sw, hm, tw > 0 (все активности учитываются в рейтинге)

Рассчитанный максимальный рейтинг ученика на программе не должен превышать Q.

Пример 1

5 4 200 1 2 3 4
Лебедев
0,3,1,1
3,3,0,0
3,0,2,2
3,1,3,2
Жуков
0,1,0,3
1,0,0,1
0,1,1,0
2,1,2,3
Белозёров
3,2,0,0
2,0,2,3
3,2,0,0
1,3,2,0
Попов
0,0,3,1
2,0,0,0
1,0,0,3
0,2,0,0
Медведев
1,0,1,1
3,2,1,0
3,2,3,2
2,1,3,0

Пример вывода:

30 24 16
Лебедев 30%
Медведев 28%
Белозёров 24%
Курс усваивается плохо

"""

data = list(map(int, input().split()))
num_students = data[0]
num_lessons = data[1]
max_rating = data[2]
classwork_coefficient = data[3]
selfwork_coefficient = data[4]
homework_coefficient = data[5]
testwork_coefficient = data[6]

# Проверка корректности вводных данных
if (num_students < 3 or num_lessons <= 0 or 
    classwork_coefficient <= 0 or selfwork_coefficient <= 0 or
    homework_coefficient <= 0 or testwork_coefficient <= 0):
    print("Во введённых данных ошибка")
    exit()

students = []

for _ in range(num_students):
    student_name = input()
    total_rating = 0
    
    for _ in range(num_lessons):
        grades = list(map(int, input().split(',')))
        classwork_grade = grades[0]
        selfwork_grade = grades[1]
        homework_grade = grades[2]
        testwork_grade = grades[3]
        
        lesson_rating = (classwork_grade * classwork_coefficient +
                         selfwork_grade * selfwork_coefficient +
                         homework_grade * homework_coefficient +
                         testwork_grade * testwork_coefficient)
        total_rating += lesson_rating
    
    # Проверка что рейтинг не превышает максимальный
    if total_rating > max_rating:
        print("Во введённых данных ошибка")
        exit()
    
    percentage = round((total_rating / max_rating) * 100)
    students.append((student_name, total_rating, percentage))

# Вычисляем статистику
ratings = [rating for _, rating, _ in students]
percentages = [percentage for _, _, percentage in students]

max_rating_value = max(percentages)
min_rating_value = min(percentages)
avg_rating_value = round(sum(percentages) / len(percentages))

# Сортируем студентов по рейтингу (убывающий порядок)
# Если рейтинги равны, сохраняем порядок ввода
students_sorted = sorted(students, 
                         key=lambda x: x[1], 
                         reverse=True)

# Вывод результатов
print(f"{max_rating_value} {avg_rating_value} {min_rating_value}")
for i in range(3):
    name, _, percentage = students_sorted[i]
    print(f"{name} {percentage}%")

# Вывод заключения о усвояемости курса
if avg_rating_value <= 50:
    print("Курс усваивается плохо")
else:
    print("Курс усваивается хорошо")

