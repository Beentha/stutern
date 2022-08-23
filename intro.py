# Module 1, assignment 3
# python program to find the exponentiation of a number
print("python program to find the exponentiation of a number")

x = int(input("Enter an integer number: "))
y= int(input("enter another integer number(power): "))

if y == 0:
    print(1)
else:
    x**=y
    print(x)