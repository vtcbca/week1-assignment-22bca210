#Write a python script to enter any number and print the sum of its digit.

def sum(num):
    a = 0
    for digit in str(num):
        a += int(digit)
    return a
num = int(input("Enter a number: "))
i = sum(num)

print("The sum of the digits is:", i)

