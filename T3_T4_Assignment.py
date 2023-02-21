                     #####Task 3
#####1
# list1 = [1, 33, "hello", "bye", 22.2, 55.5, 2+3j, 4+5j, 77, 99]

#####2
# list1 = [1, 2, 3, 4, 5]
# print(list1[1:4])

#####3
# given_list = [1, 2, 3, 4, 5]
# sum = 0
# product = 1
# for i in given_list:
#     sum += i
#     product *= i
# print('sum of all elements =', sum)
# print('product of all elements =', product)


#####4
# list2 = [4, 25, 9, 7, 19, 8, 23, 10]
# largest = list2[0]
# for i in list2:
#     if i > largest:
#         largest = i
# smallest = list2[0]
# for i in list2:
#     if i < smallest:
#         smallest = i
# print("Largest number:", largest)
# print("Smallest number:", smallest)

#####5
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []
# for i in list:
#     if i % 2 != 0:
#         new_list.append(i)
#     return new_list
# print("Result: ", new_list)

#####6
# numbers = list(range(1, 31))
# first_five = numbers[:5]
# last_five = numbers[-5:]
# first_and_last_five = first_five + last_five
# squared_list = [number**2 for number in first_and_last_five]
# print("Result: ", squared_list)

#####7
# list1 = [1,3,5,7,9,10]
# list2 = [2,4,6,8]
# list1[-1:] = list2
# print(list1)

#####8
# a = {1:10, 2:20}
# b = {3:30, 4:40}
# concatenate_dictionaries = {**a, **b}
# print(concatenate_dictionaries)

#####9
# n = 5
# result = {x: x*x for x in range(1, n+1)}
# print(result)

#####10
# input_numbers = input("Enter numbers: ")
# numbers_list = input_numbers.split(",")
# str_list = [str(num) for num in numbers_list]
# str_tuple = tuple(str_list)
# print("List of strings:", str_list)
# print("Tuple of strings:", str_tuple)


                     #####Task 4
#####1
# str = input("Enter a string: ")
# reverse_str = str[::-1]
# print("Reversed string:", reverse_str)

#####2
# def count_case(string):
#     upper_count = 0
#     lower_count = 0
#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#     print("No. of Uppercase characters:", upper_count)
#     print("No. of Lowercase characters:", lower_count)
# count_case("adcdEFGH")

#####3
# def unique_list(list1):
#     unique_lst = []
#     for i in list1:
#         if i not in unique_lst:
#             unique_lst.append(i)
#     return unique_lst
# list1 = [1, 2, 3, 3, 4, 5, 5, 6]
# new_list = unique_list(list1)
# print(new_list)

#####4
# str1 = input("Enter hypen-separated sequence of words:")
# words = str1.split("-")
# words.sort()
# new_str = "-".join(words)
# print(new_str)

#####5
# str1 = input("Enter a sequence of lines: ")
# words = str1.split("\n")
# all_upper_words = [word.upper() for word in words]
# new_str = "\n".join(all_upper_words)
# print(new_str)

#####6
# def sum_of_int(x, y):
#     x_int = int(x)
#     y_int = int(y)
#     res = x_int + y_int
#     print(res)
# sum_of_int(2, 4)

#####7
# def max_length_str(str1, str2):
#     if len(str1)>len(str2):
#         print(str1)
#     elif len(str1)<len(str2):
#         print(str2)
#     else:
#         print(str1)
#         print(str2)
# max_length_str("python", "java")

#####8
# def print_squares_in_tuple():
#     squares = tuple(i**2 for i in range(1, 21))
#     print(squares)
# print_squares_in_tuple()

#####9
# def showNumbers(limit):
#     for i in range(limit+1):
#         if i%2 == 0:
#             print(i, "EVEN")
#         else:
#             print(i, "ODD")
# showNumbers(4)

#####10
# even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 21)))
# print(even_numbers)

#####11
# given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, given_list))
# squared_numbers = list(map(lambda x: x**2, even_numbers))
# print(squared_numbers)

#####12
# def divide_by_zero():
#     try:
#         result = 5 / 0
#     except ZeroDivisionError:
#         print("Error: division by zero")
#         result = None
#     return result
# divide_by_zero()

#####13
# from functools import reduce
# list1 = [1, 2, 3, 4, 5, 6, 7]
# flattened = reduce(lambda x, y: 10*x + y, list1)
# print(flattened)

#####14
# numbers = range(1, 101)
# result = list(filter(lambda x: x % 3 != 0 and x % 7 == 0, numbers))
# print(result)

#####15
# list1 = [1, 2, 3, 4, 5]
# def square(x):
#     return x * x
# squared = list(map(square, list1))
# print(squared)

#####16
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

##output: 2

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
print('after f?')
a()

#output: NameError: name 'f' is not defined







