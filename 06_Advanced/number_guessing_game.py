

# Topic: Custom Exception Classes
class Error(Exception):
    pass

class ValueToLarge(Error):
    pass

class ValueToSmall(Error):
    pass

# Topic: Number Guessing Logic with Exception Handling
while True:
    try:
        n = 10
        n1 = int(input("Enter no: "))
        
        if n1 > n:
            raise ValueToLarge
        elif n1 < n:
            raise ValueToSmall
        elif n1 == n:
            print("You guessed the right number!")
            break

    except ValueToLarge:
        print("Please enter a smaller value")
    except ValueToSmall:
        print("Please enter a larger value")

# Topic: Counting Numbers from 1 to 10
n = 1
while n <= 10:
    print(n)
    n = n + 1

# Output (example run):
# Enter no: 15
# Please enter a smaller value
# Enter no: 5
# Please enter a larger value
# Enter no: 10
# You guessed the right number!
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10