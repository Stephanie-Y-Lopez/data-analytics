# Stephanie Y. Lopez Chavoya
length_InFeet = 28
width_InFeet = 30
a_box = 12
area = length_InFeet * width_InFeet
number_OfBoxes = area / a_box
print(f"The number of tile boxes that will be needed is: {number_OfBoxes:.0f}")

extra10_percent_tiles = number_OfBoxes * 0.10
total_Tiles = number_OfBoxes + extra10_percent_tiles
print(f"the total amount of tile boxes needed with 10% extra is: {total_Tiles:.0f}")