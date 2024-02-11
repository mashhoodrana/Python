# ====Chapter2===============================================================================================

# Exercise-4

width = 17
height = 12.0

x = width//2
print(x)
print(type(x))

y = width/2.0
print(y)
print(type(y))


z = height/3
print(z)
print(type(z))

a = 1+2*5
print(a)
print(type(a))

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´
# Exercise-5

value = input("Enter the temperature in Celcius: ")
V = float(value)

convert = V*9/5+32

print("The temperature in fahrenheit is", convert)

# =================================================Chapter----3========================================================

# Exercise 2

try:
    a = input("Enter Hours: ")
    b = int(a)
    print(b)
    c = input("Enter rate: ")
    d = int(b)
    print(d)

except:
    print("Error, please enter numeric input")

# ``````````````````````````````````````````````````````````````````````````````````````````````````````````

# Exercise 3

try:
    s = input("Enter score: ")
    score = float(s)

    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")
    else:
        print("Bad Score")

except:
    print("Bad score")


# ====Chapter4==================================================================================================

# Exercise 7
def computegrade(a):
    try:
        score = float(a)

        if 0.0 <= score <= 1.0:
            if score >= 0.9:
                grade = "A"
            elif score >= 0.8:
                grade = "B"
            elif score >= 0.7:
                grade = "C"
            elif score >= 0.6:
                grade = "D"
            elif score < 0.6:
                grade = "F"
        else:
            grade = "Bad Score"

    except:
        grade = "Bad Score"

    return grade


while(True):
    s = input("Enter score: ")
    print(computegrade(s))