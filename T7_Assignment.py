              #####Task 7
####1
# import math
# C = 50
# H = 30
# input_msg = input("Enter comma-separated sequence of values for D: ")
# d_values = input_msg.split(",")
# for d in d_values:
#     d = float(d)
#     q = math.sqrt((2 * C * d) / H)
#     print(f"D={d}, Q={q}")

####2
# class Shape:
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#     def area(self):
#         return self.length * self.length       
# shape = Shape()
# print("Shape area:", shape.area())
# square = Square(2)
# print("Square area:", square.area())

####3
# class SumtoZero:
#     def find_three_elements(self, nums):
#         result = []
#         n = len(nums)
#         nums.sort()
#         for i in range(n-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             l = i + 1
#             r = n - 1
#             while l < r:
#                 s = nums[i] + nums[l] + nums[r]
#                 if s < 0:
#                     l += 1
#                 elif s > 0:
#                     r -= 1
#                 else:
#                     result.append([nums[i], nums[l], nums[r]])
#                     while l < r and nums[l] == nums[l+1]:
#                         l += 1
#                     while l < r and nums[r] == nums[r-1]:
#                         r -= 1
#                     l += 1
#                     r -= 1
#         return result
# find = SumtoZero()
# nums = [-25, -10, -7, -3, 2, 4, 8, 10]
# triple_sum = find.find_three_elements(nums)
# print(triple_sum)

####4
# class Time:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
    
#     def addTime(self, other):
#         total_hours = self.hours + other.hours
#         total_minutes = self.minutes + other.minutes
#         if total_minutes >= 60:
#             total_hours += 1
#             total_minutes -= 60
#         return Time(total_hours, total_minutes)
    
#     def displayTime(self):
#         print("{:02d}:{:02d}".format(self.hours, self.minutes))
    
#     def displayMinute(self):
#         total_minutes = self.hours * 60 + self.minutes
#         print(total_minutes, "minutes")
# time1 = Time(4, 30)
# time2 = Time(2, 40)
# total_time = time1.addTime(time2)
# total_time.displayTime()  
# total_time.displayMinute()  

####5
# class Person:
#     def __init__(self, initialAge):
#         if initialAge < 0:
#             self.age = 0
#             print("Age is not valid, setting age to 0.")
#         else:
#             self.age = initialAge

#     def amIOld(self):
#         if self.age < 13:
#             print("You are young.")
#         elif self.age < 18:
#             print("You are a teenager.")
#         else:
#             print("You are old.")

#     def yearPasses(self, years):
#         self.age += years
# person = Person(10)
# person.amIOld()
# person.yearPasses(64)
# person.amIOld()
