print('Введите минимальную сумму инвестиций - X')
x = int(input ())
print('Введите количество долларов Майкла - A')
a = int(input ())
print('Введите количество долларов Ивана - B')
b = int(input ())
if a >= x and b >= x:
    print('2')
elif a >= x and b < x:
    print('Mike')
elif a < x and b >= x:
    print('Ivan')
elif a + b >= x:
    print('-1')
elif a + b < x:
     print('0')