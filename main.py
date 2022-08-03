# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
for height in student_heights:
  total_height += height  # В данном случае считаем сумму массива. Из student_heights вытягиваем все показатели, назвав их height и далее суммируем их через +=, добавляя к обозначееной ранее переменной total_height = 0 . Функция for loop проссумирует их необходимое кол-во раз.

total_students = 0
for students in student_heights:
  total_students += 1 # В данном случае считаем кол-во студентов. Из student_heights вытягиваем все показатели, назвав их students и далее, добавляя к ним 1 каждый раз (исходя из кол-ва введенных показателе) получается финальное число, которое начинает считаться от 0 (total students=0) и с добавлением 1 до получения финального кол-ва. Функция for loop добавит 1 необходимое кол-во раз.

average = round(total_height / total_students)
print(f" The average height is {average}")
