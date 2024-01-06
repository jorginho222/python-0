import random
import sys


#
# name = 'rodizio'
# min = 3
# max = 30

# print('r' in name)
# print('x' in name)

# print('Hi ' + name + ', you have ' + str(notif) + ' unread notifications')
# print(f'Hola {name}! tenes {random.randint(min, max)} notificaciones sin leer')

# print(f'La variable tiene {len(name)} caracteres')

# splitted = 'miami beach'.split(' ')
# print(splitted)

# joined = '; '.join(['pan', 'salame', 'queso'])
# print(joined)

# print('PASAME A MINISCULAS'.lower())

# print(bool(1))
# a = None

# fruits_list = ['mandarina', 'manzana', 'limon']
# print(fruits_list)
# fruits_list[0] = 'banana'
# print(fruits_list)
#
# fruits_tuple = ('mandarina', 'manzana', 'limon')
# print(fruits_tuple)

# names_set = {'ricardo', 'roen', 'garcia'}
# names_set.add('carlos')
# names_b_set = {'carlos', 'roen', 'pumpido'}
#
# print(names_b_set.intersection(names_set))

# ports_dict = {
#     '3455': 'Front admin',
#     '8977': 'Front mant',
#     '5444': 'Back sysv'
# }
# print(ports_dict['4006'])
# ports_dict['8092'] = 'BDD sysv'
# ports_dict['4006'] = 'Back mant'
#
# ports_dict.pop('4007')
# print(ports_dict.keys())
# print(ports_dict.values())


# lista = [1, 2, 3]
# lista.insert(2, 'elemento')
# print(lista)
#
# print(3 in lista)
# print(5 in lista)

# print(tuple('abcde'))

# my_list = [10,1,2,3,4,4,5,9,3,8,7]
#
# mySet = set(my_list)
# print(mySet)

# listorti = ['pino', 'rama', 'arbol', 'cana', 'pozo', 'jardin', 'mesa', 'roca']

# cadaDos = listorti[::2]
# print(cadaDos)
#
# cadaDosReverseConTope = listorti[:-4:-2]
# print(cadaDosReverseConTope)
#
# conRango = listorti[1:3:1]
# print(conRango)

# customSlice = slice(2, 9, 2)
# print(listorti[customSlice])

# listortiCopy = listorti[:]  # making a copy
# listortiCopy.append('ducha')
# print(listorti)
# print(listortiCopy)

# custom_range = range(-10, 0)
#
# custom_list = list(custom_range)
# print(custom_list)
# custom_list = custom_list[::2]
# print(custom_list)

# lista = [1, 2, 3, 4, 5]
#
# for i in lista[0:4]:
#     print(i)

# for x in range(3, 9, 2):
#     print(x)

# dic = {
#     'a': 1,
#     'b': 'a',
#     'c': 3
# }

# for x in dic:
#     print(x)
#
# for key, val in dic.items():
#     print(key, val)

# for val in dic.values():
#     if type(val) == str:
#         print(val.upper())
#     else:
#         print(val)

# count = 3
#
# while count <= 13:
#     print(count)
#     count += 1

# results = []
#
# for i in range(10):
#     square = i * i
#     results.append(square)
#
# print(results)

# results = [x * x for x in range(10)]  # comprehension
#
# print(results)

# dict_comp = {i: i * i for i in range(1, 10, 2)}
# print(dict_comp)

# gen_comp = (3 * x + 5 for x in range(10))
#
# for x in gen_comp:
#     print(x, end=", ")
#
# names = ['John', 'Ricky', 'Paul', 'George', 'Bob', 'Ringo', 'Mick', 'Keith', 'Charlie', 'Bill']
# filtered_names = [name for name in names if name[0] in 'CK']
# print(filtered_names)


# def pionono_function(ingredientes=['jamon'], capas=1):
#     print(ingredientes, capas)
#     another_func()
#
#
# def another_func():
#     print('holu')
#
#
# pionono_function(capas=3)

# def add_to_list(list):
#     list.append(1)

#
# list = []
#
# add_to_list(list.copy())
# add_to_list(list.copy())
#
# print(list)
#
# def func_a():
#     return func_b()
#
# def func_b():
#     return "hello from func b!"
#
# print(func_a())

