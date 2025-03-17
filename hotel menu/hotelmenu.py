#DEFINE THE MENU OF RESTO
menu = {
    'pizaa':40, 
    'pasta':50,
    'burger':60,
    'salad':70,
    'cofee':80
}

print(menu)

#greet
print("Welcome to our resto")
print("pizaa:rs40\npasta:rs50\nberger:rs60\nsalad:70\ncofee:80\n")

order_total=0
#50+60=110

item_1 = input("enter the name of item you want")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1}has been added to ypur order")

else:
 print ("orderrd item{item_1} is not available yet")
another_order = input("do you want anothe item ?(yes/no)")
if another_order == "YES":
    item_2 = input("enter the 2nd item name :")
    if item_2 in menu:
        order_total += menu[item+2]
        print(f"item{item_2}has been added")
    else:
        print(f"ordered item {item_2 }is not availabel")    
print (f"the tota amount of items is {order_total}")

