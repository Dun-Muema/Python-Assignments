
#logical Operatiors


from doctest import Example
from re import I


age = int(input("Enter your age: "))
if age>18:
    print("Adult")
else:
    print("Child")
    
#if someone is a child or tenager or adult
age = int(input("Enter your age: 2"))
if age>0 and age<12:
    print("Child")
elif age>=12 and age<19:
    print("Teenager")
elif age>=20 and age<59:
    print("Adult")
else:
    print("Senior Citizen")
    
print("Hello World")


#loop
# for when you are iterating through every element of a list
#while  - iterates until a certain condition is met


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")
    

# while loop
#example 1
counter = 0
while counter<10:
    print(counter)
    counter+=1

#control flows for loops
#break, continue, pass
#Example 1 - Break, used to exit a loop prematurely.
for num in range(0,11):
    if num ==5:
        break
    print(num)
#Example 2 - break, used to skip the current iteration and move to the next one.
fruits = ["apple", "banana", "cherry","mango","orange"]
for fruit in fruits:
    if fruit ==["mango"]:
        break
    print(fruit)
    
#continue Example 3

for num in range(0,11):
    if num ==5:
        continue
    print(num)
    
#pass Example 4 - Pass is a placeholder that does nothing. It can be used when a statement is syntactically required but no action is needed.
for num in range(0,11):
    if num ==5:
        pass
    print(num)
    

#list comprehension
#is a shortcut  for creating lists from a loop
#Example 1 - Calculate squares of numbers from 0 to 5
squares = [i**2 for i in range(1,6)]
print(squares)

#Example 2 - Cubes
cubes = [i**3 for i in range(1,16)]
print(cubes)

#even numbers betweer 1 to 50
even_numbers= [i for i in range(1,51) if i%2==0]
print(even_numbers)

#odd numbers between 1 to 50
odd_numbers= [i for i in range(1,51) if i%2!=0]
print(odd_numbers)

#Prime numbers between 1 to 100
