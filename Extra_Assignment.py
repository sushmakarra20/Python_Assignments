                        #####Extra Task
####1
# x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# access_list_1 = x[5][:4]
# print(access_list_1)

# access_list_2 = x[-3:-1]
# print(access_list_2)

# access_list_3 = x[::2] + [x[-2]]
# print(access_list_3)  

# access_list_4 = [x[::-1]]
# print(access_list_4)  

# access_list_5 = [x[5][5][0]]
# print(access_list_5)

# access_list_6 = x[5][5][2:2]
# print(access_list_6)  

####2
#Python 3
# numbers_range_python3 = print(list(range(1000)))
## numbers_range_python2 = range(1000)
## numbers_xrange_python2 = xrange(1000)

####3
#How Tuple is beneficial as compared to the list?
# Tuples are immutable. So accessing and manipulating data in a tuple is faster than in a list.
#  This is because tuples do not need to reallocate memory for resizing like lists do.
# Tuples can be used as keys in dictionaries, whereas lists cannot.
#  This is because dictionary keys must be hashable(immutable).
# Tuples are more secure than lists for storing sensitive data, 
#  as they can't be changed by malicious code after they are created(immutable).
# Tuples can be used to assign multiple variables at once.
#  Example: x, y = (15, 20)

####4
# for i in range(1, 101):
#     if i % 3 == 0 and i % 2 == 0:
#         print(i)

####5
# def vowels_in_reverse_string(string):
#     vowels = "aeiouAEIOU"
#     v_indices = []
#     res = ""
#     for i in range(len(string)-1, -1, -1):
#         if string[i] in vowels:
#             res += string[i]
#             v_indices.append(str(i))
#     return res, v_indices
# str1 = "Python Training"
# reversed_vowels, vowel_indices = vowels_in_reverse_string(str1)
# print("Reversed string: " + reversed_vowels)
# print("Vowel indices: " + ", ".join(vowel_indices))

####6
# string = "hello my name is abcde"
# words = string.split()
# for word in words:
#     if len(word) % 2 == 0:
#         print(word)

####7
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
# result_number = 8
# for i in range(len(x)):
#     for j in range(i + 1, len(x)):
#         if x[i] + x[j] == result_number:
#             print("({0}, {1})".format(x[i], x[j]))

####8
# even_list = []
# odd_list = []
# while len(even_list) < 5 or len(odd_list) < 5:
#     num = int(input("Enter a number between 1 and 50: "))
#     if num < 1 or num > 50:
#         print("Invalid input, try again.")
#         continue
#     if num % 2 == 0:
#         if len(even_list) < 5:
#             even_list.append(num)
#             if len(even_list) == 5:
#                 even_sum = sum(even_list)
#                 even_max = max(even_list)
#                 print("Even list:", even_list)
#                 print("Even sum:", even_sum)
#                 print("Even max:", even_max)
#     else:
#         if len(odd_list) < 5:
#             odd_list.append(num)
#             if len(odd_list) == 5:
#                 odd_sum = sum(odd_list)
#                 odd_max = max(odd_list)
#                 print("Odd list:", odd_list)
#                 print("Odd sum:", odd_sum)
#                 print("Odd max:", odd_max)

####9
# string = input("Enter an alphanumeric string: ")
# char = input("Enter a character: ")
# count = 0
# for c in string:
#     if c.isalpha() and c == char:
#         count += 1
# print(char + "=" + str(count))

####10
t1 = (1, 2, 3, 4, 5)
even_t1 = tuple(x for x in t1 if x % 2 == 0)
print(even_t1)

