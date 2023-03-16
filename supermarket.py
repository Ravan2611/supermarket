


# Task 18
# complete mini project super market bill generation.



user_name=input("enter u r name")
ramu_name=["ramu","sagar","kiran"]
if user_name in ramu_name:
    print("yes")
else:
    print("no")
list=''' 
Rice   Rs  20/kg
sugar  Rs  50/kg
salt   Rs  20/kg
oil    Rs  100/liter
paneer Rs  120/kg
maggi  Rs  40/kg
boost  Rs  100/each
chilli Rs  60/kg
'''
# declaration
totalprice=0
finalprice=0
# rates for items
items={"Rice":20,
"sugar":50,
"salt":20,
"oil":100,
"paneer":120,
"maggi":40,
"boost":100,
"chilli":60
}
option=int(input("for list of items press 1:"))
if option==1:
 print(list)
 for i in range(len(items)):
    inp1=int(input("if u want to buy press 1 or 2 for exit : "))
    if inp1==2:
        break
    if inp1==1:
     item=input("enter u r items:")
quantity=int(input("enter u r quantity:"))
if item in items.keys():
    price =quantity*(items[item])
totalprice+=price
gst=(totalprice*5)/100
finalprice=gst+totalprice
# bill generation 
inp=input(" enter the bill items yes or no:")
if inp=="yes":
    pass
if finalprice!=0:

  print(15*"/","Ravan maharaj",15*"/")
  print(20*" ","srilanka")
  print("user_name:",user_name,30*" ","date:",)
  print(30*"=")
  print("sno",9*" ","items",9*" ","quantity",4*" ","price")
  print(25*" ","totalprice","Rs",totalprice)
print("gst amt",25*" ","Rs",gst)
print(30*"=")
print(25*" ","finalprice","Rs",finalprice)
print(30*"=")
print(25*" ","thanks for visiting")
print(30*"=")


    
    




    







