#!/bin/python3

#Print strings
print("Hello World\n")
print("\n")
print('Hello World')

#Do MATH
print (50+50/10)
print((50**2)+10) #print 50 squared + 10 = 2510
print(50%6) #print remainder of division
print(50/6) #print float
print(50//6) #print integer part only

#Methods
test_string = "This is a test 123 stRing"
print(test_string)
print(test_string.upper())
print(test_string.lower())
print(test_string.title())

#Functions
def who_am_i():
    name ="John"
    age = "30"
    print("My name is " + name + " and I am " + str(age) + " years old")

who_am_i()

def add_100(number):
    number = number+100
    print(number)
    return number

result = add_100(123)

#Lists - Have brackets []
names_list = ["John", "Jack", "James", "Stark"]
print(names_list[1:]) # print from 1 to end
print(names_list[:2]) #print until index 2
print(names_list[-1]) #print last index

names_list.append("Jill")
print(names_list)
names_list.insert(1, "Jane")
print(names_list)




