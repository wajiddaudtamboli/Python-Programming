

# Topic: Counting Occurrences in List
list1 = [1, 2, 3, 4, 4, 4, 1]
print(list1.count(4))

# Topic: Accessing List Element in Loop
l = [5, 6, 7, 8, 9]
for i in l:
    print(l[2])

# Topic: Star Pattern Printing
n = int(input("Enter your no: "))
for i in range(0, n):
    for j in range(0, i):
        print("*", end=" ")
    print()

# Topic: Printing Even Numbers
for i in range(0, 10):
    if i % 2 == 0:
        print(i)

# Topic: Finding Matching Numbers in List
n = int(input("Enter your no: "))
l = [1, 2, 4, 1, 2, 1, 4, 4, 3, 4]
for i in l:
    if i == n:
        print(i)

# Output (example run with n=4):
# 3
# 7
# 7
# 7
# 7
# 7
# Enter your no: 4
# *
# * *
# * * *
# 0
# 2
# 4
# 6
# 8
# Enter your no: 4
# 4
# 4
# 4
# 4