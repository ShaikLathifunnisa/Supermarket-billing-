
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

from datetime import datetime

name=input("enter your name:")
#list of items
lists='''
rice - 20Rs/kg
sugar - 30Rs/kg
salt - 20Rs/kg
pulses-150/kg
oil - 80Rs/lit
Ghee-800/lit
Detergent-400/kg
Coffee Powder-250/kg
Milk Packet-75/lit
Curd-70/lit
Cheese-200/kg
paneer - 110Rs/kg
maggi - 50Rs/kg
boost - 90Rs/each
collgate - 85Rs/each
Shampoo-150/each
water Bottle-20/each
'''

# we will define in predefine 
#intially we define just like a declaration
price=0
pricelist=[]
totalprice=0
finalfinalprice=0
ilist=[] # items ki list
qlist=[] #quantity list
plist=[] #price list
 
#rates which give life to above display data
items={'rice':20,
       'sugar':30,
       'salt':20,
       'pulses':150,
       'oil':80,
       'Ghee':800,
       'Detergent':400,
       'Coffee Powder':250,
       'Milk Packet':75,
       'Curd':70,
       'Cheese':200,
       'paneer':110,
       'maggi':50,
       'boost':90,
       'collgate':85,
       'Shampoo':150,
       'water Bottle':20}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
# if i want to buy we will write forloop
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or press 2 for exit :"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
         print("sorry you entered item is not available")
    
        inp=input("can i bill the items yes or no :")
if inp=="yes":
        pass
        if finalamount!=0:
           print(25*"=","lathifa supermarket",25*"=")
           print(28*" ","shaik")
           print("Name:",name,30*" ","Date:",datetime.now())
           print(75*"-")
           print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
           for i in range(len(pricelist)):
            print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'Totalamount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*"-",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")

            # Payment Details
            payment_mode = input("Enter payment mode (Cash/Credit Card/Debit Card): ")
            if payment_mode.lower() == "cash":
                print("Payment successful. Please collect your cash receipt.")
            elif payment_mode.lower() == "credit card":
                card_number = input("Enter your credit card number: ")
                cvv = input("Enter your credit card CVV: ")
                print("Payment successful. Your credit card has been charged.")
            elif payment_mode.lower() == "debit card":
                card_number = input("Enter your debit card number: ")
                cvv = input("Enter your debit card CVV: ")
                print("Payment successful. Your debit card has been charged.")
            else:
                print("Invalid payment mode. Please try again.")