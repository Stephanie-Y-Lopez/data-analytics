#Stephanie Y. Lopez Chavoya
#Description: This script tests various numerical 
#               conversion techniques.
#Author: Sam Q. Newprogrammer

a = "101.1"
b = "55"
c = "402 Stevens"
d ='Number 5'

a_int = a
b_int = b
c_int = c
d_int = d

print (a_int)
print (b_int)
print(c_int)
print(d_int)

#Cast as interger
a_integer = int(float(a))
b_integer = int(b)
#c_integer = int(c) value error because it contains text
#d_ineager = int(d) value error because it contains text

#Cast as float
a_float = float(a)
b_float = float(b)
#c_float = float(c) value error because it contains text
#d_float = float(d) value error because it contains text

#Cast as float then int
a_float_integer = int(float(a))
b_float_integer = int(float(b))
#c_float_integer = int(float(c)) value error because it contains text
#d_float_integer = int(float(d)) value error because it contains text

#Slicing
casting_a = a[0:102]
casting_b = b[0:56]
casting_c = c[0:3]
casting_d = d[7:8]

#Displaying slice
print (casting_a.strip())
print (casting_b)
print (casting_c)
print (casting_d.strip())