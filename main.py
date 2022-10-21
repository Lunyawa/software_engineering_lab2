def calc(znak, a, b):
    if (znak == '+'):
        return a + b
    return "ОШИБКА"

znak = input("Введите знак -> ")
a = int(input("Введите первое число = "))
b = int(input("Введите второе число = "))
print(calc(znak, a, b))