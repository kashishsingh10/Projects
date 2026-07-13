'''------------------------------GROCERY BILLING SYSTEM USING DICTIONARY------------------------------'''

items={
    "rice":500,
    "oil":600,
    "wheat":370
}
total_bill=0
while True:
    item=input("Enter your item:")
    quantity=int(input("Enter quantity of item"))
    if item in items:
        total_bill+=items[item]*quantity
    else:
        print("Item is not available")
    choice=input("add another item(yes/no):")
    if choice == "no":
        break
if total_bill>500:
    discount=total_bill*0.10
else:
    discount=0
final_amount = total_bill-discount
print("Total Bill=",total_bill)
print("Discount=",discount)
print("Final Amount=",final_amount)

'''--------------------------------GROCERY BILLING SYSTEM------------------------------------'''
total=0 
while True:
    item=input("Enter your Item:")
    quantity=int(input("Enter Quantity of Item:"))
    rice=200
    dal=300
    oil=500
    if (item=="rice"):
        total+=200*quantity
    elif(item=="dal"):
        total+=300*quantity
    elif(item=="oil"):
        total+=500*quantity
    else:
        print("Item not available")
    choice=input("add another item(yes/no)=")
    if choice =="no":
        break
print("Total Bill:",total)
if (total>500):
    discount=((0.10*total))
    print("10% DISCOUNT:",discount)
    bill=total-discount
    print("Total Amount after Discount:",bill)