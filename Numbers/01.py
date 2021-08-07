
# 1) print(sys.getsizeof(3 ** 9090001) / (1024 * 1024))   # Сколько мегабайт памяти занимает данное выражение

# 2) print(4**4**4)  # Самое большое число с тремя 4 используя стандартные математические операции

# 3) Напишите функцию pos_add(a, b), которая возвращает положительное значение сложения двух целых чисел.

# def pos_add(a, b):
#    return abs(a + b)

# print(pos_add(2, -3))

# 4) Определите функцию foo(a), которая возвращает результат целочисленного и по модулю деления любого целого числа на -11.

# def foo(a):
# integer = a // -11
# module = a % -11
# return integer, module
# b = divmod(a, -11)
# return b

# print(foo(-77))

# 5) Напишите функцию num_sum(a), принимающую любое значение.
# Если это целое число, то возвратить сумму его чисел.
# В противном случае возвращается фраза «Это не целое число».

def num_sum(a):
   # 1. Определяем принадлежность значения 'a' к целому числу, но не к булеву типу
   if isinstance(a, int) and not isinstance(a, bool):
       # 2. Преобразуем число в положительное, а потом - строку
       a_to_str = str(abs(a))
       # 3. Задаем начальную сумму 0
       s = 0
       # 4. В цикле складываем все числа
       for i in a_to_str:
           s += int(i)
       return s
   return 'Это не целое число'

# Тесты
print(num_sum(-146))
print(num_sum('-11'))
print(num_sum(True))
