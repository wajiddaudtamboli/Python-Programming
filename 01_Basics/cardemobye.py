# Car Showroom Program - Calculate Car Price with Discount and GST

print("WELCOME TO GANDHI SHOWROOM")
print("AVAILABLE CARS: DZIRE, BALENO, CRYSTA")

a = 1000000
print("SWIFT DZIRE CAR PRICE =", a)

b = 9900000
print("BALENO CAR PRICE =", b)

c = 2500000
print("INNOVA CRYSTA PRICE =", c)

nameofcar = str(input("ENTER A CAR NAME TO BUY: "))

print("NOTE: DIWALI SPECIAL DISCOUNT IS 6%")

price = int(input("ENTER THE PRICE OF CAR YOU BUY: "))

disc = 6
print("DISCOUNT IS 6%")

discprice = price * disc / 100
print("DISCOUNTED PRICE ON CAR IS =", discprice)

total = price - discprice
print("PRICE NOT INCLUDING GST =", total)

gst = 2
print("GST IS 2%")

gstiscar = total * gst / 100
print("GST AMOUNT ON THIS CAR IS =", gstiscar)

finalprice = gstiscar + total
print("ON ROAD PRICE OF CAR IS =", finalprice)

print("THANK YOU! VISIT AGAIN GANDHI MOTORS")




