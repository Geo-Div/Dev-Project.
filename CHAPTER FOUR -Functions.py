Exercise 4: What is the purpose of the “def” keyword in Python?
Answer:
b) It indicates the start of a function


Exercise 5: What will the following Python program print out?
def fred():
print("Zap")
def jane():
print("ABC")
jane()
fred()
jane()
Answer:
d) ABC Zap ABC


Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Answer:
hrs = float(input("Enter Hours: "))
rt = float(input("Enter Rate: "))
pay = computepay(hrs, rt)
print("Pay;" pay)

def computepay (hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        pay = regular_pay + overtime_pay
    else:
    pay = hours * rate
return pay


Exercise 7: Rewrite the grade program from the previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade as a
string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input

Answer:
try:
    score = float(input("Enter score: "))
except ValueError:
    print("Bad score")
    quit()

def computegrade(score):
    if score > 1.0:
        return ("Bad score:", bad )
    elif score >= 0.9:
        return ("A:", a)
    elif score >= 0.8
        return ("B:", b)
    elif score >= 0.7:
        return ("C:, c")
    elif score >= 0.6:
        return ("D:, d")
    elif score =< 0.0:
        return ("F:, f")
    else:
        return("Bad score:, bad")

print("computegrade(score)")