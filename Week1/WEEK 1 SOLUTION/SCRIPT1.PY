#Write a python script to enter any number and check its prime or not.

def a(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if a(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

            
