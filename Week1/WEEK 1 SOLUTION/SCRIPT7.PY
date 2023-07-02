#Write a python script to enter any string, replace vowel with its position number.

def replacevowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = s.lower()
    a = ""

    for index, char in enumerate(s, start=0):
        if char in vowels:
            a += str(index)
        else:
            a += char

    return a
s = input("Enter a string: ")
a = replacevowels(s)

print("Modified string:", a)
