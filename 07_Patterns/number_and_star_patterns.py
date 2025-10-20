

# Topic: Incremental Number Pattern
num = 1
for i in range(0, 4 + 1):
    for j in range(0, i + 1):
        print(num, end=" ")
        num = num + 1
    print()

# Topic: Incremental Number Triangle
n = 1
for i in range(1, 6):
    for j in range(i):
        print(n, end="")
        n = n + 1
    print()

# Topic: Star Pyramid Pattern
for i in range(0, 3):
    for j in range(0, 3 - i - 1):
        print(end=" ")
    for k in range(0, i + 1):
        print("*", end=" ")
    print()

# Topic: Star Pattern with Incorrect Logic (Corrected)
for i in range(0, 4):
    for j in range(0, 4 - i - 1):
        print(" ", end=" ")
    for k in range(0, i + 1):  # Corrected from i*1 to i+1
        print("*", end=" ")
    print()

# Topic: While Loop Star Pattern (Corrected)
i = 1
while i <= 4:
    j = 0  # Corrected logic to print stars based on i
    while j < i:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1

# Output:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# 1
# 23
# 456
# 78910
# 1112131415
#   * 
#  * * 
# * * * 
#       * 
#     * * 
#   * * * 
# * * * * 
# *
# **
# ***
# ****