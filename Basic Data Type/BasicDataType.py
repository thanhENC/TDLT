#Basics data types:

# from os import system, name
# from time import sleep

# '''
# convert cTemp to fTemp
# '''

# def clear():
#     # for windows
#     if name == 'nt':
#         #_ = system('cls')
#         system('cls')
  
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         #_ = system('clear')
#         system('clear')

# def cTempToFConverter():
#     while True:
#         cTemp = input("Input C temperature: ")
#         if cTemp:
#             try:
#                 cTemp = float(cTemp)
#                 fTemp = round(cTemp*1.8+32, 2)
#                 sleep(2)
#                 clear()
#                 print(f"{cTemp}C is converted to {fTemp}F.")
#                 break
#             except Exception as e:
#                 print(e)
#         else:
#             print("C temperature is empty.")
#             continue


# def main():
#     cTempToFConverter()

# if __name__ == "__main__":
#     main()



# from datetime import datetime

# def calculateAge():
#     while True:
#         birthYear = input('Input your birth year: ')
#         if birthYear:
#             try:
#                 birthYear = int(birthYear)
#                 now = datetime.now()
#                 age = now.year - birthYear
#                 if age < 0 or age > 150:
#                     raise Exception
#                 else:
#                     print(f'You are {age}')
#                     break
#             except:
#                 print(f'Your input is invalid.')
#         else:
#             print('Your input is empty.')

def checkPrimeNum(num):
    if num >= 1:
        for i in range(2, num):
            if num % i == 0:
                print(f'{num} is not a prime number.')
                break
        else:
            print(f'{num} is a prime number.')
    else:
        print(f'{num} is not a prime number.')

# def fibonacci(N):
#     if N < 0:
#         return 'Incorrect input.'
    
    

def main():
    checkPrimeNum(int(input()))

if __name__ == '__main__':
    main()

def staircase(n):
    # Write your code here
    for _ in range(n):
        print(" "*(n-1-_), end='')
        print("#"*(_+1), end='')
        print("")

def main():
    n = int(input().strip())
    staircase(n)
        
if __name__ == '__main__':
    main()

x, k = map(int, input().split())
P = eval(input())
print(P==k)
            