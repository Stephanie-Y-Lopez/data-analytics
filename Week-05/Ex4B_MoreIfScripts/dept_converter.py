#Stephanie Y. Lopez Chavoya

def departments_by_code (dept_code):
    if dept_code == 1:
        dept_name = "Marketing"
    elif dept_code == 5:
        dept_name = "Human Resources"
    elif dept_code == 10:
        dept_name = "Accounting"
    elif dept_code == 12:
        dept_name = "Legal"
    elif dept_code == 18:
        dept_name = "IT"
    elif dept_code == 20:
        dept_name = "Customer Relations"
    else:
        dept_name = "Unknown Department"
        
    print(f"Code {dept_code}: {dept_name}")

#Testing
test_codes = [1, 5, 10, 12, 18, 20, 67]

for code in test_codes:
    departments_by_code(code)
