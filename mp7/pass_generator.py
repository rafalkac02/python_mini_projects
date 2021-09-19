import random
import string

pword = ''

# random length from 8 to 16
l = random.randint(8,16)

# types of characters - letter (lower- or uppercase), number, special char
types = ['l', 'n', 's']


for c in range(l):
    # pick random type of charachter
    c = random.choice(types)
    if c == 'l':
        pword += random.choice(string.ascii_letters)
    elif c == 'n':
        pword += str(random.randrange(10))
    else:
        pword += random.choice(string.punctuation)

print(pword)

random = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(random.randint(8,16))])
print(random)