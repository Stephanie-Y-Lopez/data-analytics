#Stephanie Y. Lopez Chavoya
current_hour = float(input("Please enter the current time military clock style (EX: 3:00pm = 15:00): "))

def greeting_based_on_time (current_hour):
    if 5 <= current_hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good day!"
    elif 18 <= current_hour < 23:
        greeting = "Good evening!"
    elif (23 <= current_hour <= 24) or (0 <= current_hour < 5):
        greeting = "What are you doing up so late?"
    else:
        greeting = "Invalid time, please enter a valid hour (0-24)."
        
    print(f"Greeting: {current_hour}: {greeting_based_on_time}")

    #Calling the function
    greeting_based_on_time(current_hour)
