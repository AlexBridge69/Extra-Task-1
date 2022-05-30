# Написать программу преобразования двоичного числа в десятичное.
Number_2_system = input('Введите число, состоящее только из 0 и 1: ')
for i in range(2, 10):
    if (Number_2_system.find(str(i)) != -1):
        print('Во введённом числе не должны быть цифры, отличные от 0 и 1!')
        exit()  # если во введённом числе
    # присутствует хотя бы одна цифра,
    # отличная от 0 и 1, то
    # программа завершается принудительно.

Len_number = len(Number_2_system) - 1
Number_10_system = 0
for letter in Number_2_system:
    Number_10_system += int(letter) * 2**Len_number
    Len_number -= 1
print(Number_10_system)
