import random
import string

def newpass(letter_count, sym_count, dig_count):
    password = []
    password.extend([random.choice(string.ascii_letters) for x in range(int(letter_count))])
    password.extend([random.choice(string.punctuation) for x in range(int(sym_count))])
    password.extend([random.choice(string.digits) for x in range(int(dig_count))])
    random.shuffle(password)
    return password

print('Welcome to the PyPassword Generator!')
letnum = input('How many letters would you like in your password?\n')
symnum = input('How many symbols would you like?\n')
dignum = input('How many number would you like?\n')

passgen = newpass(letnum, symnum, dignum)

print(f'Here is your password {"".join(passgen)}')