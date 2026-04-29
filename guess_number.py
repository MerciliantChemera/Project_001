from random import randrange as rnd

secret_value = rnd(101)

print('Я загадал число от 1 до 100, сможешь его угадать?', end='\n')

while True:
    print('Введите число:')
    guess_value = int(input())

    if guess_value < secret_value:
        print('Загаданное число больше, пробуй ещё раз')
    elif guess_value > secret_value:
        print('Загаданное число меньше, пробуй ещё раз')
    else:
        print('Молодец, я загадал именно ', str(secret_value))
        break