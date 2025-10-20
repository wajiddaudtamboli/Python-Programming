

# Topic: Upper Triangle Pattern
for i in range(5):
    for j in range(i):
        print("*", end="")
    print()

# Topic: Lower Triangle Pattern
for i in range(5):
    for j in range(i):
        print("*", end="")
    print()

# Topic: Pyramid Pattern
for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()

# Topic: Lower Pyramid Pattern with Mixed Characters
for i in range(5):
    for j in range(i):
        print("8", end="")
    for k in range(5 - i):
        print("*", end=" ")
    print()

# Output:
# 
# *
# **
# ***
# ****
# 
# *
# **
# ***
# ****
#      1
#     * 2
#    * * 3
#   * * * 4
#  * * * * 5
# * * * * *
# 8* * * *
# 88* * *
# 888* *
# 8888*