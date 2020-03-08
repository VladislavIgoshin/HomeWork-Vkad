import tkinter
import PIL
a = int(input("Введите выручку фирмы "))
b = int(input("Введите издержер фирмы "))
l = 0
r = a - b
if r > l:
             print("Доход составляет ", r)
             k = int(input("Введите число работников "))
             h = r // k
             print("Прибыль физмы на одного работника ", h)
else:
        print("Убыток составляет ", r)