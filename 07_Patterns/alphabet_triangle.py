# Alphabet Triangle and Pyramid Patterns



# Pattern 1: Alphabet Triangle with Numbers
for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print(chr(65), end=" ")
    print(i + 1)

"""
Output:
    1
   A 2
  A A 3
 A A A 4
A A A A 5
"""

print("-" * 30)

# Pattern 2: Alphabet Pyramid with While Loop
i = 0
while i <= 5:
    c = 65
    j = 0
    while j <= 5 - i:
        print(" ", end="")
        j += 1
    k = 0
    while k < i:
        print(chr(c), end=" ")
        k += 1
        c += 1
    i += 1
    print()

"""
Output:
      
     A 
    A B 
   A B C 
  A B C D 
 A B C D E 
A B C D E F 
"""

print("-" * 30)

# Pattern 3: Inverted Alphabet Pyramid with While Loop
i = 0
while i <= 5:
    c = 65
    j = 0
    while j < i:
        print(" ", end="")
        j += 1
    k = 0
    while k <= 5 - i:
        print(chr(c), end=" ")
        k += 1
        c += 1
    i += 1
    print()

"""
Output:
A B C D E F 
 A B C D E 
  A B C D 
   A B C 
    A B 
     A 
      
"""