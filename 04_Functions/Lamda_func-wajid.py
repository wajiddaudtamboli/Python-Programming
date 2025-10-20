#LAMBDA FUNC:

#In User Defined Func.:
'''
def add(x,y):
    z=x+y
    print(z)
add(85,5)
'''

#Lambda:
#Add:
'''
add=lambda x,y:x+y
print(add(85,5))
'''

#SQRT:
'''
sqrt=lambda x:x**2
print(sqrt(5))
'''

#Area:
'''
area_rect=lambda l,b:l*b
print("The area of rectangle is: ")
print(area_rect(10,20))
'''

#Cube:
'''
cube=lambda x:x**x
print(cube(3))
'''

#Filter->Searching:
#Even Cond. finder in a list:
'''
l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
'''

#Positive or negative:
'''
l=[1,-1,34,-28,-7,23,-91,51,8,-10]
l=list(filter(lambda x:x>0,l))
print("The positive no. in a list are:")
print(l)
'''

#Map->Setting Cond. for all print:
#Sqrt of a list: 
'''
l=[1,2,3,4,5,6,7,8,9,10]
l=list(map(lambda x:x*2,l))
print(l)
'''

#Cube rt of a list:
'''
l=[1,2,3,4,5,6,7,8,9,10]
l=list(map(lambda x:x**x,l))
print("The cube root of the elements presented in this list is: ")
print(l)
'''

#REV OF STRING:
'''
def string_rev(str1):
    rstr1=''
    index=len(str1)
    while index>0:
        rstr1 +=str1[index-1]
        index=index-1
    return rstr1
print(string_rev("1234abcd"))
'''

#DICTIONARY:
#UPPER/LOWER CASE:
'''
def str_test(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Original String: ",s)
    print("No. of Upper case characters: ",d["UPPER_CASE"])
    print("No. of Lower case characters: ",d["LOWER_CASE"])
str_test("The quick Brown fox")
'''

#UNIQUE LIST:
'''
def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x    
print(unique_list([1,2,3,3,3,4,5]))        
'''

#CONCATENATE FOLOWING DICTIONARIES TO CREATE A NEW ONE:
'''
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in(dic1,dic2,dic3):dic4.update(d)
print(dic4)
'''

#LARGEST NO. FROM A LIST:
'''
def max_num(l):
    max=l[0]
    for a in l:
        if a>max:
            max=a
    return max    
print(max_num([1,2,-8,0]))
'''

#Round every no. & print total sum multiplied by the length of the list:
'''
nums=[22.2,4.0,-16.22,-9.10,11.00,-12.22,14.20,-5.20,17.50]
print("Original list: ",nums)
print("Result: ")
length=len(nums)
print(sum(list(map(round,nums))*length))
'''

#Rev strings values using lamda:
'''
def rev_str_list(lst):
    result=list(map(lambda x:"".join(reversed(x)),lst))
    return result
colors_lst=["Red","Green","Blue","white","Black"]
print("\nOriginal lists:\n",colors_lst)
print("Rev str list:")
print(rev_str_list(colors_lst))
'''

#Sort a given mixed list of integers and str using lamada:
'''
def sort(mix_lst):
    mix_lst.sort(key=lambda e:(isinstance(e,str),e))
    return mix_lst
mix_lst=[19,'red',12,'green','blue',10,'white','green',1]
print("Original list:\n")
print(mix_lst)
print("\nAfter Sort:\n")
print(sort(mix_lst))
'''

#Remove none value from a given list using lambda:
'''
def remove_None(nums):
    result=filter(lambda v:v is not None,nums)
    return list(result)
nums=[12,0,None,23,None,-55,234,98,None,0,6,-12,None]
print("Org. list:\n")
print(nums)
print("\nAfter removing none:\n")
print(remove_None(nums))
'''

#Divisible by 19 or 13 from a list using lambda:
'''
nums=[19,65,131,33,4,33,13,57.39,152,639,121,44,90,190]
print("Original list:\n")
print(nums)
result=list(filter(lambda x:(x%19==0 or x%13==0),nums))
print("\nNo. of the above list divisible by 19 or 13:\n")
print(result)
'''

#MAX OF 3 NO.
'''
def max_2(x,y):
    if x>y:
        return x
    return y
def max_3(x,y,z):
    return max_2(x,max_2(y,z))
print(max_3(3,6,-5))
'''

#COUNT NO. OF STR:
'''
def match_words(words):
    ctr=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
        return ctr    
print(match_words(['abc','xyz','aba','1221']))
'''

#SORT A LIST OF TUPLES USING LAMBDA:
'''
subject_marks=[('eng',88),('sci',90),('maths',97),('sst',80)]
print("Org list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x:x[1])
print("\nSorting the list of tuples:")
print(subject_marks)
'''
