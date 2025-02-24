# Restraurent Management platform where people can order from menu

# Menu
menu = {
    "Burger" : 70,
    "Pizza" : 150,
    "Cold Coffee" : 50,
    "Cold Drink" : 30,
    "Cake" : 200
}

print(f"Please order something from the menu : ")
for i in menu :
    print(i, menu[i])

order_amount = 0

item = input("What do you want to order : ")

if item in menu :
    order_amount += menu[item]
    print(f"{item} has been added to cart")
else :
    print("Item not in cart. Please order something else")
    


choice = input("DO you want to order something else ? (Yes/No) : ")

while choice == "Yes" :
    item = input("What do you want to order : ")
    if item in menu :
        print(f"{item} has been added to cart")
        order_amount += menu[item]
        choice = input("DO you want to order something else ? (Yes/No) : ")
    else :
        print("Item is not in cart")


print(f"Total amount to be paid : {order_amount}")