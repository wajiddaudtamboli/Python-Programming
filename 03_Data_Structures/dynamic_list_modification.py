

# Topic: Modifying and Appending to List
list1 = [0, 0]
count1 = 0
for val in range(3, 8):
    if count1 < len(list1):
        list1[count1] = val
        count1 += 1
    else:
        list1.append(val)
print(list1)

# Output:
# [3, 4, 5, 6, 7]