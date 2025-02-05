# python random password generator
import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# generate 12 digits including letters, numbers, and symbols
def generate_uppercase_letter():
    letter = chr(random.randint(65,90))
    return letter

def generate_lowercase_letter():
    letter = chr(random.randint(97,122))
    return letter

def generate_number():
    number = chr(random.randint(49,57))
    return number

def generate_symbol():
    symbol = chr(random.randint(36,38))
    return symbol

c1 = generate_uppercase_letter()
c2 = generate_uppercase_letter()
c3 = generate_uppercase_letter()
c4 = generate_lowercase_letter()
c5 = generate_lowercase_letter()
c6 = generate_lowercase_letter()
c7 = generate_number()
c8 = generate_number()
c9 = generate_number()
c10 = generate_symbol()
c11 = generate_symbol()
c12 = generate_symbol()

password = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12
password = shuffle(password)

print(password)