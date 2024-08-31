# This Will Be my Python Notes

# Variables , input
name = "BRUHNAME" #This is a string
age = 18  #This is a integer
isStudying = False #This is a boolean
randomNumber = 1.87 #This is a float

#If statements , for loop , while loop
if (age >= 18) :
  print ("Your'e an adult")
elif (age < 18) :
  print ("Your'e a minor")
else :
  print ("Thats not an age")

for i in range (1,6):
  print (i) #returns 1-5

count = 5
while count > 0:
  print(count)
  count -= 1 #returns 5-1

#Data structures (List, tuples , dictionaries)
#lists (mutable , ordered)
fruits = ["apple" , "banana" , "cherry"]
fruits.append("date") #append to add items to the last array
print("fruits:", fruits) #returns an array

#tuple (immutable, ordered)
coordinates = (10,20)
print ("coordinates:" , coordinates)

#dictionary (mutable, unordered , key-value pairs). Like an object in Javascript

person = {
  "name" : "Bob",
  "age" : 30,
  "city" : "New York"
}
print ("Person:" , person) #prints all of the information
print ("Name:" , person["name"]) #prints specific

#List comprehension (a concise way to create a list)
#creating a list of squares
squares = [x**2 for x in range(10)]
print (squares)

#with conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print (even_squares)

#lambda functions (Arrow function in javascript)
multiply = lambda x, y: x * y
print (multiply(5,3))

#using lambda with map()
numbers = [1,2,3,4,5]
squared = list(map(lambda x : x**2, numbers))
print (squared)

#decorators (enhancing functions)
def uppercase_decorator(func):
  def wrapper():
    result = func()
    return result.upper()
  return wrapper

@uppercase_decorator
def greet():
  return "hello, world!"

print (greet())

#with statements (managing resources)
#file handling with context manager
with open('example.txt' , "w") as file:
  file.write ("Hello, World!")
#file is automatically closed after the block

#Generators (working with large sequences)
def countdown(n):
  while  n > 0:
    yield n
    n -= 1

for number in countdown (5):
  print (number)

#type hinting, for type check
  def greet(name:str) -> str:
    return f"Hello, {name}"
  
print (greet("Alice"))

#async and await python
import asyncio

async def main():
  print ("Hello")
  await asyncio.sleep(1)
  print('World')

asyncio.run(main())


  





