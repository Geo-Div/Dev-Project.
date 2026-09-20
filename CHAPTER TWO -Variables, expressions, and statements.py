5
x = 5
x + 1
print (x + 1)
6


Exercise 2: Write a program that uses input to prompt a user for their name
and then welcomes them.

Answer:
name = input("enter your name here: Divine\n")
print("Hello",name)


Exercise 3: Write a program to prompt the user for hours and rate per hour to
compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

Answer:
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
hours = input("Enter Hours: 35 \n")
rate = input("Enter Rate: 2.75 \n")
pay = (35) * (2.75)
print = ("pay:", 96.25)


Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
For each of the following expressions, write the value of the expression and the
type (of the value of the expression).
1. width//2
2. width/2.0
3. height/3
4. 1 + 2 * 5

Answer:
Use the Python interpreter to check your answers.
width = 17
height = 12.0
width//2
width/2.0
height/3
1 + 2 * 5


Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.

Answer:
celsius = float(input("Enter a temperature in Celsius: \n"))
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)

Answer 1:
inp = input('Enter Celsius Temperature: 100 ')
fahr = float(inp)
celsius = (100 * 32.0) + 5.0
print(celsius)

Answer 2
inp = input('Enter Celsius Temperature: 100 ')
fahr = float(inp)
celsius = (100 * 9) + 32
print(celsius)