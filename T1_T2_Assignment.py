                #TASK1
#### 1
# a, b, c = 1, 2.01, "Hello"
# print("a", type(a))
# print("b", type(b))
# print("c", type(c))

#### 2 complex number
# x=5
# y=6+ 2j
# x, y = y, x
# print("x=", x)
# print("y:", y)

#### 3 Swapping variable
# x, y = 5, 6
# x, y = y, x
# print("x:", x)
# print("y:", y)
# x, y = 5, 6
# temp = x
# x = y
# y = temp
# print("x:", x)
# print("y:", y)

#### 4
# msg = print(input("Enter your message:"))  #python 3.0
# msg = raw_input("Enter your message:") #python 2.0
# print(msg)

#### 5
# num1 = int(input("Enter number between 1 to 10: "))
# num2 = int(input("Enter number between 1 to 10: "))
# print("First number is: ", num1)
# print("First number is: ", num2)
# Z = num1+num2
# result = Z + 30
# print("Result is: ", result)

#### 6
# x = 22
# print("The data type of the input is: ", type(x))

#### 7
# IWantToType = "Upper Camel Case"
# iWantToType = "Lower Camel Case"
# i_want_to_type = "Snake Case"
# # string = "i want to type"
# # UPPERCASE_VARIABLE = string.upper()
# # print(UPPERCASE_VARIABLE)
# # UPPERCASE
# UPPERCASE_VARIABLE = "UPPERCASE"

#### 8
# Yes. In Python, always the last assigned value is 
# the value stored in a variable. 

                                ###Task 2
#### 1
# def divisor_of_3or5(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "Consultadd - Python Training"
#     elif num % 3 == 0:
#         return "Consultadd"
#     elif num % 5 == 0:
#         return "Python Training"
#     else:
#         return
# number = int(input("Enter a number: "))
# res = divisor_of_3or5(number)
# if res:
#     print(res)
# else:
#     print("The number is not divisible by either 3 or 5.")

# #### 2
# print("Enter 1 for Addition")
# print("Enter 2 for Subtraction")
# print("Enter 3 for Division")
# print("Enter 4 for Multiplication")
# print("Enter 5 for Average")
# option = int(input("Choose an option:"))
# if option == 1:
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter a number:"))
#     result = num1 + num2
#     if result < 0:
#         print("NEGATIVE")
#     else:
#         print("Result:", result)
# elif option == 2:
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter a number:"))
#     result = num1 - num2
#     if result < 0:
#         print("NEGATIVE")
#     else:
#         print("Result:", result)
# elif option == 3:
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter a number:"))
#     result = num1 / num2
#     if result < 0:
#         print("NEGATIVE")
#     else:
#         print("Result:", result)
# elif option == 4:
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter a number:"))
#     result = num1 * num2
#     if result < 0:
#         print("NEGATIVE")
#     else:
#         print("Result:", result)
# elif option == 5:
#         first_number = int(input("Enter first number:"))
#         second_number = int(input("Enter second number:"))
#         Average = (first_number+second_number)/2
#         if result < 0:
#             print("NEGATIVE")
#         else:
#             print("Result:", result)
# else:
    # print("Invalid choice")


#### 4
# while True:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         print("It's Over")
#         break
#     else:
#         print("Good Going")
#         continue
#### 5
# numbers = []
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         numbers.append(i)
# print(numbers)

#### 6
# x=123
# for i in x:
#     print(i)
# #output: TypeError: 'int' object is not iterable
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#     else:
#         print(“error”)
# #output: SyntaxError: invalid character '“' (U+201C)
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break
# #output: NameError: name 'Break' is not defined  
      
#### 7
# for i in range(0, 7):
#     if i == 3 or i == 6:
#         continue
#     print(i, end=" ")

#### 8
# user_input = input("Enter a string: ")
# letters = 0
# digits = 0
# for char in user_input:
#     if char.isdigit():
#         digits += 1
#     elif char.isalpha():
#         letters += 1
# print("Letters", letters, "Digits", digits)

#### 9
# number = 100
# answer = "yes"
# while answer != "no":
#     guess = int(input("Guess the lucky number: "))
#     if guess == number:
#         print("You've got it! The lucky number is", number)
#         break
#     answer = input("Do you want to guess again? (yes/no) ").lower()
# print("Thank you for playing!")

#### 10
# lucky_num = 100
# count = 1
# while count <= 5:
#     guess = int(input("Guess the lucky number: "))
#     if guess == lucky_num:
#         print("Good guess!")
#     else:
#         print("Try again!")
#     count += 1
# print("Game over!")

#### 11
# lucky_num = 100
# count = 1
# while count <= 5:
#     guess = int(input("Guess the lucky number: "))
#     if guess == lucky_num:
#         print("Good guess!")
#         break
#     else:
#         print("Try again!")
#     count += 1
# if guess != lucky_num:
#     print("Sorry but that was not very successful")




