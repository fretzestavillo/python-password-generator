import random

number = int(input("Enter the number of passwords to generate: "))
length = int(input("Enter the length of passwords to generate: "))


char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789`~!@#$%^&*()-_+={}[]|\:;\"'<>,.?/"

for _ in range(number):
    password = ''
    for _ in range(length):
        password += random.choice(char)
    print('Password: ', password)
