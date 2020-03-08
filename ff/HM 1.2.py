import tkinter
import PIL
a = int(input("Введите время в секундах: "))
b = a // 60
c = b // 60
print(f"Время: {c}:{b}:{a}")