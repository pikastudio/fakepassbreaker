import random
import string

letters = list(string.ascii_lowercase + string.ascii_uppercase)

def a(c):
    return "attempt " + str(c) + " " + random.choice(letters)

def b():
    return random.choice(letters)

print("------------------------------------------------")
print("|         password breaker by zeke             |")
print("------------------------------------------------")
a = input("|                   enter a ip:                 ")
print("------------------------------------------------")
b = input("|                    username:                  ")
print("------------------------------------------------")

c = 0
passwords = [] 

for i in range(5000):
    line = a(c)
    c += 1
    for j in range(10):
        line += b()
    passwords.append(line)
    print(line)  

line = a(c)
c += 1
for j in range(10):
    line += b()
passwords.append(line)
print(line)

# Example: show how many were stored
print("------------------------------------------------")
print("password for " + a + "@" + b + ": " +  passwords[-1].split()[2])
print("run ssh " + a + "@" + b + " with the password: " + passwords[-1].split()[2])
print("------------------------------------------------")
