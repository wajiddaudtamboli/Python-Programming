# File Handling Operations

# File Operations Examples

# Opening and Reading a File
'''
file=open("nkcoet.txt","r")
print(file.read())
'''

# Writing to a File
'''
file = open("nkcoet.txt", "w")
file.write("This is a sample file content. Created for demonstration.")
file.close()
'''

# Appending to a File
'''
file2 = open("nkcoet1.txt", "a")
file2.write("\n\nThis is additional content appended to the file.")
file2 = open("nkcoet1.txt", "r")
print(file2.read())
file2.close()
'''

# Reading a File Line by Line
'''
for each in file:
    print(each)
file.close()
'''

# Reading File Line by Line
'''
print(file.readline())
file.close()
'''

# Fibonacci Series to File
f = open('fib.txt', 'w')
n1 = 0
n2 = 1
i = 1
n = int(input("Enter the range of fibonacci: "))
f.write("The fibonacci series is:\n\n")
f.write(str(n1) + "\n")
f.write(str(n2) + "\n")
while i < n:
    fib = n1 + n2
    n1 = n2
    n2 = fib
    i += 1
    f.write(str(fib) + "\n")
f.write("\n\nTask completed successfully")
print("Successfully executed")
f.close()   
