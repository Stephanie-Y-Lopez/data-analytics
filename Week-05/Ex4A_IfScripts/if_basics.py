#Stephanie Y. Lopez Chavoya

x = 100
y = 20

#1
if x / y == 5:
        print("x is divided by 5")
        x = 1
else:
     print("are the variables set up correctly?")

#2
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print("Whoops, x equals", x)

#3
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")

#4
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")


print(f"The final value of x is {x} and the final value of y is {y}")