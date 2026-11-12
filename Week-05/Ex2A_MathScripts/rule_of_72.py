# Stephanie Y. Lopez Chavoya
account_balance = 12000
# interest_rate = 0.11
#Using this problem for user input on the interest rate,
interest_rate = float(input("Please enter your interest rate (as a decimal, EX: 0.10 for 10%): "))
years_to_double = 72 / (interest_rate * 100)
account_balance_after_years = account_balance * (1 + interest_rate) ** years_to_double
print("At a", "{:.2f}".format(interest_rate * 100), "% interest rate, your savings account will be worth", "${:.2f}".format(account_balance_after_years), "in", "{:.1f}".format(years_to_double), "years.")
