# def count_substring(string, sub_string):
#     count = 0
#     i = string.find(sub_string)
#     while i != -1:
#         count += 1
#         i += 1
#         i = string[i:].find(sub_string)

#     return count
    

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)



# def binary(n):
#     return bin(n).replace("0b", "")

# def octal(n):
#     return oct(n).replace("0o", "")

# def hexadecimal(n):
#     return hex(n).replace("0x", "")

# def print_formatted(n):
#     w = len("{0:b}".format(n))
#     for _ in range(1, n+1):
#         print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(_, width=w))


# if __name__ =="__main__":
#     n = int(input())
#     print_formatted(n)



# def is_vowel(letter):
#     return letter in ['a', 'e', 'i', 'o', 'u', 'y']

# def score_words(words):
#     score = 0
#     for word in words:
#         num_vowels = 0
#         for letter in word:
#             if is_vowel(letter):
#                 num_vowels += 1
#         if num_vowels % 2 == 0:
#             score += 2
#         else:
#             score += 1
#     return score

# n = int(input())
# words = input().split()
# print(score_words(words))




def solve(s):
    arr = [char for char in s]
    if str(arr[0]).isalpha():
        arr[0] = str(arr[0]).upper()
    
    for index in range(1, len(arr)):
        if arr[index-1] == ' ' and arr[index].isalpha():
            arr[index] = str(arr[index]).upper()
    
    return ''.join(arr)


s = input()

result = solve(s)

print(result)