my_dict = {"name": "Van An", "content": "Programming", "city": "HoChiMinh"}
print(my_dict)

my_list2 = dict(name="Van An", content="Programming", city="Sai Gon")
print(my_list2)

#Access items
content_in_dict = my_dict["content"]
print(content_in_dict)

#check for keys
#use if..in..
if "age" in my_dict:
    print(my_dict["age"])
else:
    print("No key found")

#use try except
try:
    print(my_dict["age"])
except:
    print("No key found")

#add and change items (key-value) pairs
#add a new key
my_dict["email"] = "thanhenc@gmail.com"
print(my_dict)
#or overwrite the value on existing key
my_dict["email"] = "thanhenc@itbclub.onmicrosoft.com"
print(my_dict)
#delete a key-value pair
#del my_dict["city"]
print(my_dict)

#delete a key-value pair with pop, pop return the value of removed key
print("Popped value: " + my_dict.pop("city"))
print(my_dict)

#delete items with .popitem()