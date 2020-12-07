import random

identifier = input("Введите ваш идентификатор: ")
p = len(identifier)^2%10+len(identifier)^3%10+1
src_pass = {
    'numbers': '1234567890',
    'letters': 'abcefghijklmnopqrsuvwxyz',
    'chars': '+-*/!@#$%^&()[]()_;:|/,.',
}

password = (f"{random.choice(src_pass['numbers'])}{random.choice(src_pass['numbers'])}{random.choice(src_pass['numbers'])}")
password += (f"{random.choice(src_pass['chars'])}{random.choice(src_pass['chars'])}{random.choice(src_pass['numbers'])}")
password += (f"{random.choice(src_pass['letters'].upper())}{random.choice(src_pass['letters'][p])}")

print(password)