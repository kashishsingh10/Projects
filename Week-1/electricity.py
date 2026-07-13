'''----------------------------ELECTRICITY BILL CALCULATOR-----------------------------------'''
name=(input("Enter Your Name:"))
units=int(input("Enter Consumed Units: "))
if units<=100:
    total=units*5
else: 
    total=(100*5)+((units-100)*8)
print("Total Bill:",total) 