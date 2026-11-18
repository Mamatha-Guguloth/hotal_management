menu={
    'pizza':30,
    'burger':20,
    'pasta':25,
    'salad':15,
    'soda':10
}
print("welcome to mammu restaurant")
print('menu items :')
for item, price in menu.items():
    print(f"{item}: ${price}")
order_total=0
while True:
    item_name=input("enter the item you want to order:")
    if item_name in menu:
        order_total+=menu[item_name]
        print(f" your item {item_name} has been added to your order. Total: ${order_total}")
    else:
        print("sorry, we don't have that item on the menu.")
    anther_item=input("do you want to order another item? (yes/no):")
    if anther_item == "no":
        break
    # if anther_item=="yes":
    #     item_2=input("enter the your second item: ")

    # if item_2 in menu:
    #     order_total+=menu[item_2]
    #     print(f" your item {item_2} has been added to your order. Total: ${order_total}")

    # else:
    #     print("sorry we don't have that item on the menu.")
print(f"your total order amount is: ${order_total}")
