#Stephanie Y. Lopez Chavoya
pay_rate = float(input("Please enter how much money you make per hour: "))
hours_worked = float(input("Please enter how many hours you worked this week: "))
overtime_pay_rate = pay_rate * 1.5

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    gross_pay = regular_pay + (overtime_hours * overtime_pay_rate)
else:
    gross_pay = pay_rate * hours_worked

print(f"Your gross pay is: ${gross_pay:.2f}")

if hours_worked < 40:
    print("Under 40 hours")
if hours_worked == 40:
    print("Exactly 40 hours")
if hours_worked > 40:
    print("Over 40 hours")