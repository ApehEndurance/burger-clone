#print("First program - python print function")
#print("It is declared like this:")
#print("print('what to print' )")

#print("String manipulation exercise")
#print('String maipultion is done with "+" Sign ')
#print('e.g print("Hello" + "Jenny")')
#print("New line can be created with a backslash and n")

#name=input("What is your name? ")
#print("Hello " + name + "," + " how are you?")
#print( len(name))

#Swipe Number

#a=input("Enter value of a ")
#b=input("Enter value of b ")

#temp = a
#a = b
#b = temp

#print("a=" + a)
#print("b=" + b)

# Type casting
"""length=len("Jenny Lecture")
print("your nmae has " + str(length) + " character")"""

"""
num1=input("Enter num1")
num2=input("Enter num2")
sum= int(num1) + int(num2)
print(sum)"""

#BMI
#weight= input("Enter your weight in kg: ")
#height= input("Enter your height in meters: ")
#bmi= int(weight) // float(height) **2
#print(int(bmi))


#a=5
#print(id(a))

"""a=8
print(id(a))
print(a is a)"""

#print(round(11.5))
#print(round(12.5))
"""
import random
import time


numbers= ['1', '2', '3', '4', '5', '6']
characters= ['@', '%', '&', '(']
letter= ['a', 'b', 'c', 'd']

password= '' .join(random.sample(numbers,6)) + random.choice(characters) + random.choice(letter)
print(password)"""

"""
numbers=['1', '2', '3', '4', '5', '6']

user1=input("User1 press r to rool a dice: ")
first_rool =(random.choice(numbers))
second_rool =(random.choice(numbers))
user1_dice = int(first_rool) + int(second_rool)
time.sleep(3)
print("You roll " + first_rool + " and " + second_rool + " = " + str(user1_dice))

user2 =input("User2 press r to role a dice: ")
first_rool =(random.choice(numbers))
second_rool =(random.choice(numbers))
user2_dice = int(first_rool) + int(second_rool)
time.sleep(3)
print("You roll " + first_rool + " and " + second_rool + "=" + str(user2_dice))

if user1_dice == user2_dice:
    print("Its a tie")
elif user1_dice > user2_dice:
    print("User1 won")
elif user1_dice < user2_dice:
    print("User2 won")

print("Start over")
"""





"""numbers =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

tele ='0603'
phone_number = '' .join(random.sample(numbers,7))

print(tele + phone_number)
"""
"""
number = input ("Enter nmuber: ")

if number%2 == 0:
    print("This is and even number")
elif number%2 != 0:
    print("This is an odd number")"""




"""
year = int(input("Enter Year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(str(year) + " is a leap year")
else:
    print(str(year) + " Is not a leap year")"""

"""
elif year % 4 != 0 and year % 100 == 0:
    print(str(year) + " Is not a leap year")"""



"""weight = input("What is your weight: ")
unit = input("type L for LBS or K for KG: ")

if unit == 'K':
    kilogram = int(weight) * 0.45
    print(kilogram)
elif unit == 'L':
    pound = int(weight) * 0.45359237
    print(pound)
"""
"""import random
lucky_number = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9',]
random_number= (random.choice(lucky_number))
count = 0
max_count = 3

while count < max_count:
    number_entered = int(input('input a number from 1 to 9: '))
    count += 1
    if number_entered == random_number and count < max_count:
     print("You Won!")
     break
    elif number_entered != random_number and count == 1:
        print('try agian ')
print("You loose, the lucky number is: " + random_number)
"""

"""essay = input('input oyur long sentence here ....')


words = len(essay.split())
print(words)"""


#create len function using loop
"""
a = [1, 2, 3, 4, 5, 6]
number = 0
for item in a:
    number += item
print(number)

"""
#Len function

"""a = [1, 2, 3, 4, 5, 6, 'john']
number = 0
for item in a:
    number += 1
print(number)
"""
#find the highest value in a list

"""a = [-10, 2, 3, 4, 5, 6,]
lowest_number = 1
for items in a:
    if items < lowest_number:
        lowest_number = items
print(lowest_number)
"""

"""
balance = 20000
while balance >= 10000:
    transfer = input('how muxh would you like to tranfer')
    new = balance-int(transfer)
    if transfer <= balance:
        print('Your new balance is : ' + str(new))
"""

a = [2,6]
sum = 0
sum_total= 0
for x in a:
    sum_total += x
    sum += 1
    average=sum_total//sum

print(average)