import random
import string

def newpass(letter_count, sym_count, dig_count):
    password = []
    password.extend(list((string.ascii_letters[random.randint(0, len(string.ascii_letters)-1 )]) for x in range(len(letter_count))))
    print(password)
    password.extend(list((string.punctuation[random.randint(0, len(string.punctuation)-1)]) for x in range(len(sym_count))))
    print(password)
    password.extend(list((string.digits[random.randint(0, len(string.digits)-1)]) for x in range(len(dig_count))))
    print(password)
    return random.shuffle(password)

print('Welcome to the PyPassword Generator!')
letnum = input('How many letters would you like in your password?\n')
symnum = input('How many symbols would you like?\n')
dignum = input('How many number would you like?\n')

passgen = newpass(letnum, symnum, dignum)

print(f'Here is your password {passgen}')