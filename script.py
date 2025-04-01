matte = 1 + 1 +16
print(matte)


import time
def seconds_counter():
    seconds_passed = 0
    while True:
        print(f"Seconds passed: {seconds_passed}")
        time.sleep(3)
        seconds_passed += 3

seconds_counter()

