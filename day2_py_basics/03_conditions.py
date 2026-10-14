#Even/Odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#---------------------------------------------------------------

#Largest of 3
a, b, c = map(int, input("Enter three numbers: ").split())
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)

#----------------------------------------------------------------

#Grade Calculator
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade O")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

#----------------------------------------------------------------

# Leap Year
year = int(input("Enter a year: "))
if( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")