#Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.

def a(num):
    m = str(num)
    
    if m == m[::-1]:
        return True
    else:
        return False

num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    if a(num):
        print("The number is a palindrome!")
    else:
        print("The number is not a palindrome.")
else:
    print("Invalid input. Please enter an integer number.")

