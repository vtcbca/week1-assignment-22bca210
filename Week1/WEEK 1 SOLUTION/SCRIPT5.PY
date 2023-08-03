#Write a python script to enter any string and count vowel.

def vowel(s):
    vowels = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}

    vowelcount = 0

    for char in s:
        if char in vowels:
            vowelcount += 1

    return vowelcount

s = input("Enter a string: ")
vowelcount = vowel(s)
print("Number of vowels:", vowelcount)
