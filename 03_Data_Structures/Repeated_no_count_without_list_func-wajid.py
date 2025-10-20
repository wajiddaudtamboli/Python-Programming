#Counting the elements in list without using list func
def repeated_no():
    counts={}
    for num in sequence:
        if num in counts:
            counts[num]+=1
        else:
            counts[num]=+1
    for num, count in counts.items():
        print("Number num={0} occurs count={1} times",format(num,count))
sequence=int(input("Enter the elements in list"))
repeated_no(sequence)
