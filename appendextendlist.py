"""Create an empty list called shopping_cart. Add the items 'milk', 'bread', and 'eggs' to it using the .append() method.
   Then use .extend() to add ['butter', 'cheese'] to the list. Print the final list."""

shopping_cart=[]

shopping_cart.append("milk")

shopping_cart.append("eggs")

newlist=['butter', 'cheese']


shopping_cart.extend(newlist)

print(shopping_cart)