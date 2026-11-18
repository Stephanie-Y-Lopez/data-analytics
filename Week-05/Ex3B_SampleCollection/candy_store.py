#Stephanie Y. Lopez Chavoya
candies = ("Gummy Bears", "Taffy", "Lollipops")
candy_flavors = ("Watermelon", "Blueberry", "Mango", "Green Apple")

# Making combos
candy_options = {
    f"{candy_flavors[0]} {candies[0]}",
    f"{candy_flavors[1]} {candies[1]}",
    f"{candy_flavors[2]} {candies[2]}",
    f"{candy_flavors[0]} {candies[2]}",
    f"{candy_flavors[1]} {candies[0]}"}

# 4. Print the output message and the set contents
print("Today’s candy options include:")
print(candy_options)