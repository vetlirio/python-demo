# Create a loop that counts from 1-20
# 1. make it simply count and print it

def simple(end):
    for i in range(end):
        print(i)

simple(21)


# 2. create same loop, but without a function


for i in range(21):
    print(i)    


# 3. create same loop, but total of all the numbers

def simple(end):
    total = 0 
    for i in range(end):
        total += i
    return total

print(simple(21))

    