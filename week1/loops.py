# loops

fruits = ["Apple", "Pear", "Grapes"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} Pie")


for number in range(1, 11):
  print (number)

for number in range(1, 11, 3):
  print (number)

total = 0
for number in range(1, 101):
  total += number
print (total)

total = 0
for number in range(1, 101):
  if (number % 2 == 0):
    total += number
print (total)


# The FizzBuzz Game
# Write your code here 👇
for number in range (1, 101):
  if (number % 3 == 0) and (number % 5 ==0):
    print ("FizzBuzz")
  elif number % 3 == 0:
    print ("Fizz")
  elif number % 5 == 0:
    print ("Buzz")
  else: 
    print (number)