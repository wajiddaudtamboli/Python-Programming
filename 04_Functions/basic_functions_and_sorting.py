

# Topic: Basic Function Definition
def add(x, y):
    z = x + y
    print(z)
add(5, 6)

# Topic: Sorting List of Tuples
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social Science', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)

# Topic: Lambda Function for Addition
add = lambda x, y: x + y
print(add(5, 3))

# Output:
# 11
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social Science', 82)]
# Sorting the List of Tuples:
# [('Social Science', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
# 8