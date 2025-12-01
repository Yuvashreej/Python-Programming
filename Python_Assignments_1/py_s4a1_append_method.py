# You’re helping build a simple grocery shopping assistant app. Users can add items they want to buy to a shopping cart (list). Each time the user enters an item, it gets added to the cart using the append() method.

# Your task is to:

# Create an empty list (shopping cart).
# Ask the user to enter items they want to buy.
# Use a loop to append each item to the list.
# Show the final list at the end.

shopping_cart=[]
total_of_items = int(input("enter total no of items to be added into the grocery list"))

for i in range(total_of_items):
    items= input("enter the items :")
    shopping_cart.append(items)
print(shopping_cart)

#  or

shopping_cart=[]

while True:
     items= input("enter the items :")
     if items.lower() == "done":
         break
     shopping_cart.append(items)
print(shopping_cart)

