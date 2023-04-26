# Create a list called menu, which should contain at least 4 items in the cafe.
menu = ["coffee", "tea", "cake", "sandwich"]

# Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
stock = {"coffee": 42, "tea": 57, "cake": 20, "sandwich": 15}

# Create another dictionary called price, which should contain the prices foreach item on your menu
price = {"coffee": 2.45, "tea": 2.25, "cake": 3.50, "sandwich": 4.20}

# Next, calculate the total_stock worth in the cafe. You will need to remember to loop through 
# the appropriate dictionaries and lists to do this.

total_stock = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value
    # PLUS: print out the worth value of each item in the stock.
    print(f"- {item} stock is worth £{item_value:.2f}")

# Finally, print out the result of your calculation.
print(f"\nThe TOTAL stock is worth £{total_stock:.2f}")