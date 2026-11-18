#stephanie Y. Lopez Chavoya
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

#Printing the names in all lower case
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

#Priting the names with the first letter being capitalized
print(name_1.title())
print(name_2.title())
print(name_3.title())

#Printing without the money symbol
print(salary_1.replace("$", " "))
print(salary_2.replace("$", " "))

salary_1_int = int(salary_1.replace("$", " ").replace(",", " "))
salary_2_int = int(salary_2.replace("$", " ").replace(",", " "))
print(salary_1_int)
print(salary_2_int)