#Stephanie Y. Lopez Chavoya

def departments_by_cod(dept_code):
    match dept_code:
        case 1:
            dept_name = "Marketing"
        case 5:
            dept_name = "Human Resources"
        case 10:
            dept_name = "Accounting"
        case 12:
            dept_name = "Legal"
        case 18:
            dept_name = "IT"
        case 20:
            dept_name = "Customer Relations"
        case _:
            dept_name = "Unknown Department"
            
    print(f"Code {dept_code}: {dept_name}")

#Testiing
test_codes = [1, 5, 10, 12, 18, 20, 30]

for code in test_codes:
    departments_by_cod(code)
