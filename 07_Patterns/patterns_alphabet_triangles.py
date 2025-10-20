# Alphabet Triangle Patterns

# Pattern 1: Alphabet Triangle with Numbers
for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print(chr(65), end=" ")
    print(i + 1)

print("-" * 20)

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

print("-" * 20)

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