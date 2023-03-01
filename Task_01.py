# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
lenght_list = int(input("Введите длину списка: "))
searching_number = int(input("Введите число которе необходимо найти: "))
my_list = [random.randint(1, 100) for _ in range(lenght_list)]
print(my_list)
count = 0
for item in range(lenght_list):
    if searching_number == my_list[item]:
        count += 1
if count > 0:
    print(f'Заданное число встречается в списке {count} раз(а)')
else:
    print('Заданного числа нет в этом списке.')
    my_dict = {}
    for item in my_list:
        my_dict[item] = my_dict.get(item, 0) + 1
    print(my_dict)
    lesser_num = searching_number
    higher_num = searching_number
    while (my_dict.get(lesser_num) == None) and (my_dict.get(higher_num) == None):
        lesser_num -= 1
        higher_num += 1
        if my_dict.get(lesser_num) != None:
            print('{} - ближайшее наибольшее число, встречается: {} раз(а)'.format(lesser_num, my_dict[lesser_num]))
        elif my_dict.get(higher_num) != None:
            print('{} - ближайшее число, встречается: {} раз(а)'.format(higher_num, my_dict[higher_num]))