"""name = input("What is you name? ")
print("Hi " + name)
"""
a_person = input("What is you name? ")

color = input("What color do you like? ")

print(a_person + " likes " + color)


# Accessing items 0-3
basic_items = ["a", "b" , "c", "D"]
print(basic_items)

basic_items = ["a", "b" , "c", "D"]
print(basic_items[1])

basic_items = ["a", "b" , "c", "D"]
print(basic_items[3])

# -1 = starting at the end 1=b 0=a -1=d
basic_items = ["a", "b" , "c", "D"]
print(basic_items[-1])


# change the item in the list

basic_items = ["a", "b" , "c", "D"]
print(basic_items[1])

basic_items[1] = "B"
print(basic_items)

basic_items[3] = "dd"
print(basic_items)
