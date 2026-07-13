'''------------------------------MOVIE TICKET BOOKING SYSTEM--------------------------------'''
name=input("Enter Your Name:")
ticket=int(input("Enter Number of Tickets: "))
price=200
if (ticket>5):
    price*=ticket
    print("Total Cost : ",price)
    discount=((0.10*price))
    print("10% DISCOUNT : ",discount)
    total=price-discount
    print("Cost after Discount :",total)
else:
    total=ticket*price
    print("Total Amount : ",total)