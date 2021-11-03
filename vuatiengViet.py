import string
import random

def password_generator(strName):
    # LETTERS = string.ascii_letters
    # DIGITS = string.digits
    # PUNCTUATION = string.punctuation

    printable = strName.replace(' ', '')
    
    #print(strName)
    printable = list(printable)
    random.shuffle(printable)
    print(printable)
    #password = random.choices(printable)
    password = "/ ".join(printable)

    return password

# def get_password_length():
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
    # password_length = get_password_length()
    strName = ''
    while strName != "STOP":
        print('/')
        strName = input("Name: ")
        randomWord = password_generator(strName)
        print(randomWord)

if __name__ == '__main__':
    main()