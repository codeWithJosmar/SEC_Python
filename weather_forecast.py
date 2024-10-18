temperature = float(input("Enter temperature in Celsius: "))
rain_chance = float(input("Enter the percentage chance of rain: "))

if rain_chance > 50 or temperature < 15:
    print("Carry an umbrella!")
else:
    print("No need for an umbrella today.")