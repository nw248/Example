operation = input("Введите действие : ")
a = float(input("Введите значение 1 : "))
b = float(input("Введите значение 2 : "))

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    if b != 0:
        print(a / b)
    else:
        print("Ошибка: Деление на ноль")
else:
    print("НЕВЕРНАЯ ОПЕРАЦИЯ")