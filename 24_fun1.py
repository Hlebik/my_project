def fun_1 (math):
    if -2.4 <= math <= 5.7:
        return math ** 2
    else:
        return 4
    
math = float(input("Введите значение:"))
print("значение равно:", fun_1(math))
