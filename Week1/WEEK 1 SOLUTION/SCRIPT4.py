#Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.

def arms(num):
    a = str(num)
    digits = len(a)
    sum = 0
    for digit in a:
        sum += int(digit) ** digits
    if num == sum:
        return True
    else:
        return False

number = input("Enter a number: ")
if number.isdigit():
    number = int(number)
    if arms(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")
else:
    print("Invalid input. Please enter a valid integer number.")
