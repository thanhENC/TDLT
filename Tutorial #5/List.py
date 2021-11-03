# def isPalindrome(self, s: str) -> bool:
#     if s:
#         result = []
#         for c in s.lower():
#             if c.isalnum():
#                 result.append(c)
#         return result == result[::-1]

#     else:
#         return False

# print(isPalindrome("A man, a plan, a canal: Panama", "A man, a plan, a canal: Panama"))


# presidents = ["Washington", "Adams", "Jefferson", "Madision", "Monroe", "Adams", "Jack"]

# for index, president in enumerate(presidents, 1):
#     print(f'President #{index}: {president}')


# LIST COMPREHENSIONS


# even_numbers = [item for item in range(10) if item %2 == 0]
# print(even_numbers)

# TRANSACTIONS = [100, 150, 200, 180]
# TAX_RATE = 0.08
# SERVICE_CHARGE = 0.07

# def get_price_tax_service(bill):
#     return bill*(1+TAX_RATE+SERVICE_CHARGE)

# print([float(f"{get_price_tax_service(bill):.2f}") for bill in TRANSACTIONS])


# wizards = ['Harry Potter', 'Ron', 'Hermione']
# pets = ['Hedwig', 'Scabber', 'Crookshank']
# for index, (wiz, pet) in enumerate(zip(wizards, pets), 1):
#     print(f'{index}. {wiz} has {pet}.')


# 2D array / Matrix
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# #combi columns with zip and *:
# y = [x for x in zip(*matrix)]
# print(y[1][2])

# single_list = [matrix[row][col]
#                for row in range(len(matrix)) for col in range(len(matrix))]
# print(single_list)

# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         print(matrix[row][col], end=' ')
#     print()


# txt = "Hello, welcome to my world welcome."

# x = txt.find("welcome")

# print(x)

# txt = txt.replace("welcome", "hello")

# print(txt)


txt = "508.00"

x = txt.isdigit()

print(x)