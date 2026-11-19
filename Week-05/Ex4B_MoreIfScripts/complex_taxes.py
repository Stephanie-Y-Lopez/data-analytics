#Stephanie Y. Lopez Chavoya
pay_rate = 10.00
hours_worked = 45
filing_status = "single"

#Income
if hours_worked <= 40:
    weekly_gross_pay = hours_worked * pay_rate
else:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    weekly_gross_pay = regular_pay + overtime_pay
annual_gross_pay = weekly_gross_pay * 52

#Filing status
if filing_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
    
if filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    print("Invalid filing status.")
    tax_rate = 0.0

#Weekly tax and net pay
weekly_tax = weekly_gross_pay * tax_rate
net_pay = weekly_gross_pay - weekly_tax

print(f"You worked: {hours_worked} in this period. Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is $475 Your filing status is {filing_status} Your tax withholding for the week is ${weekly_tax:.2f} Your net pay is ${net_pay}")
