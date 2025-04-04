#We need Item, Number of item, and price
while(True):
    item = input("What Item would you like to add to store : ")

    if(item=="No"):
             
             break

    quantity = input("Enter the quantity of items : ")

    price= float(input("Enter price of each Item : "))

    print(f"Item name is {item}\n Quantity is {quantity} and total price is {price * float(quantity)}")

   

