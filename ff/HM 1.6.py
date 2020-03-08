import tkinter
import PIL
while True:
    a = int(input("Введите число "))
    b = int(input("Введите число "))

    t = a 
    r = 1

    while b >= t:
        t *= 1.1
        r += 1
    print(r)