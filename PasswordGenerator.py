import string
import random

length = int(input("Enter the length of Password: "))
password = ""
val = string.ascii_letters+string.digits+string.punctuation

take = random.choices(val, k=length)
for i in take:
    password += i
print(password)
