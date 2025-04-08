def print_numbers():
    for i in range(0, 100):
        print(i)
print(print_numbers())

"""Match Countdown

We need a timer to countdown the start of PvP matches in Fantasy Quest.
Assignment

In the countdown_to_start function, write a loop that counts down from 10 to 1. At each iteration, print the number with an ellipsis:

i...

However, when i is 1, it should print 1...Fight! instead.
"""

def countdown_to_start():
    for i in range (10, 1, -1):
        print (f"{i}...")
    print("1...Fight!")


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()


def contains_leather_scraps(items):
    found = False
    for item in items:
        if item == "Leather Scraps":
            found = True

def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if new_character_levels[i] > old_character_levels[i]:
            print(i)
            
            
def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far
    