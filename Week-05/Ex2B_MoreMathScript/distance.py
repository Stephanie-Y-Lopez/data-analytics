# Stephanie Y. Lopez Chavoya
import math

number_1 = 28
result = math.sqrt(number_1)
print(f"The square root of {number_1} is: {result:.2f}")

#calculating the distance between (x1,y1) and (x2,y2)
x1, y1 = 2, 8
x2, y2 = 3, 0
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")