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


# more loops 

# print 1-200 with 25 increments

for i in range(1, 201, 30):
    print(i)


# create a loop that counts down from 1.000.000 to -1.000.000 in increments of 250.000

for i in range(1000000, -1250000, -250000):
    print(i)

# same thing, but make it a function

def counting_down(start, end, step):
    for i in range(start, end, step):
        print(i)

counting_down(1000000, -1250000, -250000)


