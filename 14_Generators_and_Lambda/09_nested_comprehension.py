burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "bean", "spam"]

meals = [(burger, toppings) for burger in burgers for topping in toppings]
print(meals)

for meal in meals:
    print(meal)