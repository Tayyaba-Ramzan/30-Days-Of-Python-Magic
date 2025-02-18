# 30-Day Python Coding Challenge: From Basic to Advanced 

# Day 6: Loops - While Loop
# Question: Write a program that calculates the factorial of a number using a while loop.

# Solution:

num = int(input("Enter a number: "))

factorial = 1
i = num

while i > 0:
    factorial *= i
    i -= 1


print(f"Factorial of {num} is {factorial}")

#                            XXXXXXXXXXXXXXXXXXX