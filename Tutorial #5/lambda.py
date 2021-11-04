#Find square root of a number
# num = int(input("Enter a number: "))
# my_func = lambda x: x**0.5
# print(my_func(num))


#filter odd numbers
my_list = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 != 0, my_list)))

new_list = [item for item in my_list if item % 2 != 0]
print(new_list)