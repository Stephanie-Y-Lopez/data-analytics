#Stephnanie Y. Lopez Chavoya
fav_animals = ["Elephants", "Kiwi Bird", "Dogs", "Dingos", "Stringrays"]

print("--- Ranking ---")
for index, animal in enumerate(fav_animals, start=1):
    if index == 1:
        print(f"{index}. {animal} <- top pick!")
    else:
        print(f"{index}. {animal}")