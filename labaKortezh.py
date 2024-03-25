#задание 1

 #пользователь вводит с клавиатуры название фрутка
# #необходимо вывести на экран кол-во раз , сколько
# #фрукт встречается в кортеже в качестве элемента 
# fruit_tuple = ("банан","яблоко", "груша")
# fruit_name = input("please enter a fruit name:")

# print(f"your fruit:{fruit_name}, exist in our tuple, count: "f"{fruit_tuple.count(fruit_name)}")

#задание 2
# Добавьте к заданию 1 подсчет количества раз, когда 
# название фрукта является частью элемента. Например: 
# banana, apple, bananamango, mango, strawberry-banana.
# В примере выше banana встречается три раза
# fruit_tuple = ("банан","яблоко", "груша","апельсин","виноград","апельсин-апельсиновый","яблоко-винное")
# fruit_name = input("please enter a fruit name:")

# print(f"your fruit:{fruit_name}, exist in our tuple, count: "f"{fruit_tuple.count(fruit_name)}")

# fruit_like_part = 0

# for fruit in fruit_tuple:                                 #находит одни и те же фркуты и подсчитывает их кол-во
#     if fruit_name in fruit:
#         fruit_like_part += 1

# print(fruit_like_part)


#задание 3


# Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0 
# до N раз). Пользователь вводит с клавиатуры название 
# производителя и слово для замены. Необходимо заменить 
# в кортеже все элементы с этим названием на слово для 
# замены. Совпадение по названию должно быть полным.


# tuple_auto = ("lada","mercedes","bmw", "cherry","lada","tesla","haval")

# new_auto = input("enter new auto name: ")     #то на что будем менять
# replace_auto = input("enter auto name for replacement: ")  #то что будем изменять

# updated_tuple = tuple(new_auto if auto == replace_auto else auto 
#                       for auto in tuple_auto) #нужно читать справа на лево цикл

# print(f"updated auto tuple: {updated_tuple}")

#поменяли в кортежи одну марку машины на другую

#задание 4

# Есть кортеж с целыми числами. Нужно вывести статистику
# по количеству цифр в элементах кортежа. Например:
# ■ Одна цифра — 3 элемента;
# ■ Две цифры — 4 элемента;
# ■ Три цифры — 5 элементов.

# this_dict = {
#     "brand": "ford",
#     "model": "mustang",
#     # "year": 1964,
#     "year": 1985, # новый создан был позже , он и выведется
#     "colors": ["red", "white", "green"],
#     2: False
# }
# print(this_dict, type(this_dict))
# print(this_dict["model"])


# this_dict = dict(model = "mustang", year=1964)
# print(this_dict, type(this_dict))
 
# РЕШЕНИЕ:

# integer_tuple = (1,2,22,44,111,222,333,444,2,5,55)

# result_dict = {}

# for num in integer_tuple:
#     num_length = len(str(num))
#     if num_length in result_dict:
#         result_dict[num_length] += 1
#     else:                                              
#         result_dict[num_length] = 1
# # ■ Одна цифра — элемента;
# # ■ Две цифры — элемента;     посчитали цифры  у меня  1 цифра их 4 , 2;: 3 , 3: 4 
        
# # ■ Три цифры —  элементов.
# print(result_dict)
# print(result_dict.items())

# for length, count in result_dict.items():
#     print(f"■ {length} цифра - {count} элемента")







