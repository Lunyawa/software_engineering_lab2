def calc(znak, a, b):
    if (znak == '+'):
        return a + b
    elif (znak == '-'):
        return a - b
    elif (znak == '*'):
        return a * b
    elif (znak == '/'):
        choice = input("Вам нужно целочисленное деление? (напишите + или -)" )
        if (b == 0):
            return "Ошибка на 0 делить нельзя!"
        if (choice == '+'):
             return a // b
        else:
             return a / b
    return "ОШИБКА вы ввели не знак"

znak = input("Введите знак -> ")
a = int(input("Введите первое число = "))
b = int(input("Введите второе число = "))



print(calc(znak, a, b))