
'''
# x mode file creat
f=open("Cadd center.txt",'x')
print("file creat sucessfully")

# read mode
f=open("cadd center.txt",'r')
print("file is reading")
#print(f.read())
print(f.read(15))
print(f.readline())



# writting mode
# Add Information of 10 Students
f=open("cadd center.txt",'w')
print("file writting")

#f.write("i am omkar from solapur")
#f.close()
f.writelines(['1.','\nI am Omkareshwar','\nMY contact no. 8010322321','\nMy adderes is Bale, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from Electrical Branch'])
f.writelines(['\n2.','\nI am Mahesh','\nMY contact no. 8010322322','\nMy adderes is Bale, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from Civil Branch'])
f.writelines(['\n3.','\nI am Ram','\nMY contact no. 8010322323','\nMy adderes is Sontosh Nagur, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from Mechanical Branch'])
f.writelines(['\n4.','\nI am Raj','\nMY contact no. 8010322324','\nMy adderes is Ambica Nagur, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from Computer Branch'])
f.writelines(['\n5.','\nI am Yash','\nMY contact no. 8010322325','\nMy adderes is Laxmi, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from E&NTC Branch'])
f.writelines(['\n6.','\nI am Rahul','\nMY contact no. 8010322326','\nMy adderes is Bale, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from CSC Branch'])
f.writelines(['\n7.','\nI am Omkar','\nMY contact no. 8010322327','\nMy adderes is Bale, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from Civil Branch'])
f.writelines(['\n8.','\nI am Rajesh','\nMY contact no. 8010322328','\nMy adderes is Todkar vasti Bale, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from Electrical Branch'])
f.writelines(['\n9.','\nI am Ramesh','\nMY contact no. 8010322329','\nMy adderes is Sontosh Nagur Bale, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from Mechanical Branch'])
f.writelines(['\n10.','\nI am Samarth','\nMY contact no. 8010322320','\nMy adderes is Laxmi Bale, North Solapur, Maharashtra','\nI am from Sinhgad College of Engg','\nI am from Electronic Branch'])

f.close()


f=open("cadd center.txt",'w')
print("file writting....")

f.writelines([input('Enter Roll no.')])
f.writelines([input('Enter Your Name ')])
f.writelines([input('Enter Contact no. ')])
f.writelines([input('Enter Your Branch ')])
f.writelines([input('Enter College Name ')])
f.writelines([input('Enter Address ')])

f.close()
'''


f=open("cadd center.txt",'w')
print("file writting....")

f.writelines([input('Enter Roll no.'),'\n',input('Enter Your Name '),'\n',
              input('Enter Contact no. '),'\n',input('Enter Your Branch '),'\n',
              input('Enter College Name '),'\n',input('Enter Address ')])


f.close()
