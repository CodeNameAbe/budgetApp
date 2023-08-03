# main.py
from budgetApp import Category, create_spend_chart

# Test the Category class
food_category = Category("Food")
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")

clothing_category = Category("Clothing")
entertainment_category = Category("Entertainment")

food_category.transfer(50, clothing_category)

print(food_category)
print(clothing_category)

# Test the create_spend_chart function
categories = [food_category, clothing_category, entertainment_category]
print(create_spend_chart(categories))
