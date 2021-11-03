import string
import random

def password_generator(length=8):
    LETTERS = string.ascii_letters
    DIGITS = string.digits
    PUNCTUATION = string.punctuation

    printable = f'{LETTERS}{DIGITS}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)

    password = random.choices(printable, k=length)
    password = ''.join(password)

    return password

def get_password_length():
    length = 0
    while True:
        try:
            length = int(input('How long do you want your password: '))
            if length <= 0:
                raise Exception
            else:
                return length
        except:
            print('Input is invalid. Please input again!')

def main():
    password_length = get_password_length()
    random_password = password_generator(password_length)
    print(random_password)

if __name__ == '__main__':
    main()