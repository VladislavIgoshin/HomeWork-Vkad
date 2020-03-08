import tkinter
import PIL
while True:
    a = input("Ввведите число ")
    if a.isdigit():
     n = int(a)
     res = 0
     while n:
         t = n % 10
         if t > res:
            r = t
            n //= 10
            break
    else:
        print("ошибка ввода")
print(r)