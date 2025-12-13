import random
import string

letters = list(string.ascii_lowercase + string.ascii_uppercase)

def ez(c):
    return "attempt " + str(c) + " " + random.choice(letters)

def ez2():
    return random.choice(letters)


c = 0
passwords = []  

while True:
    line = ez(c)
    c += 1
    for j in range(10):
        line += ez2()
    passwords.append(line)
    print(line)  
