# Stephanie Y. Lopez Chavoya
people_going_on_tour = 38
charter_van_seats = 15
charter_van_cost = 250
number_of_vans_needed = people_going_on_tour / charter_van_seats
total_van_cost = number_of_vans_needed * charter_van_cost
total_paided_per_person = total_van_cost / people_going_on_tour

print(f"The number of vans needed is: {number_of_vans_needed:.0f}")
print(f"The cost per person is: ${total_paided_per_person:.2f}")

amount_of_money_collected = total_paided_per_person * people_going_on_tour
print(f"The amount of money collected is: ${amount_of_money_collected:.2f}")

print(f"The total cost for the vans is: ${total_van_cost:.2f}")

leftover_money = amount_of_money_collected - total_van_cost
print(f"The leftover money is: ${leftover_money:.2f}")