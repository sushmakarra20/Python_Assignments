              #####Task 5
####1
# try:
#     eval("x === 1")
# except SyntaxError as e:
#     print("Syntax error occurred:", e)

####2
# import sys
# if len(sys.argv) > 1:
#     file_name = sys.argv[1]
# else:
#     file_name = input("Enter file name: ")

# while True:
#     try:
#         with open(file_name, 'r') as file:
#             contents = file.read()
#             print(contents)
#             break
#     except FileNotFoundError:
#         print("File not found.")
#         file_name = input("Enter file name: ")
#     except:
#         print("An error occurred.")
#         break
####3
# num = input("Enter a number: ")
# try:
#     if len(num) != 4:
#         raise ValueError("The length is too short/long !!! Please provide only four digits")
#     num = int(num)
#     print("Number entered:", num)
# except ValueError as e:
#     print(e)

####4
# def get_user_input():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     retype_password = input("Re-type your password: ")
#     return (username, password, retype_password)

# def validate_user_input(username, password, retype_password):
#     if password != retype_password:
#         print("Passwords do not match.")
#         return False
#     elif len(password) < 8:
#         print("Password is too short.")
#         return False
#     elif username != "your_username" or password != "your_password":
#         print("Invalid username or password.")
#         return False
#     else:
#         return True

# for i in range(3):
#     username, password, retype_password = get_user_input()
#     if validate_user_input(username, password, retype_password):
#         print("Login successful!")
#         break
#     else:
#         print("Please try again.")
#     if i == 2:
#         print("You have exceeded the maximum number of attempts.")
#         exit()

####5
# done

####6
# with open('doc.txt', 'r') as file:
#     content = file.read()
#     words = content.split()
#     even_words = [word for word in words if len(word) % 2 == 0]
#     even_string = ' '.join(even_words)
#     print(even_string)


              #####Task 6
####1
# string = "Hello World"
# uppercase_chars = [char for char in string if char.isupper()]
# print(uppercase_chars)

####2
# students = ['Smit', 'Jaya', 'Rayyan']
# subjects = ['CSE', 'Networking', 'Operating System']

#       # Using a for loop
# student_subject_dict = {}
# for i in range(len(students)):
#     student_subject_dict[students[i]] = subjects[i]
# print(student_subject_dict)

#         # Using dictionary comprehension
# student_subject_dict = {students[i]: subjects[i] for i in range(len(students))}
# print(student_subject_dict)

#         # Using zip function
# student_subject_dict = dict(zip(students, subjects))
# print(student_subject_dict)

####3

####4
# def reverse_string(string):
#     yield from string[::-1]
# input_string = "Consultadd Training"
# output_string = ''.join(reverse_string(input_string))
# print(output_string)

####5
# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper
# def say_hello():
#     print("Hello!")
# say_hello = my_decorator(say_hello)
# say_hello()
