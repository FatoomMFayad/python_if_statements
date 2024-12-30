temprature = float(input("Enter the temperature in Celsius: "))
if temprature < 0:
    print("Freezing weather")
elif 0<= temprature < 10:
    print("Very Cold weather")
elif 10 <= temprature < 20:
    print("Cold weather")
elif 20 <= temprature < 30:
    print("Normal in Temp")
elif 30 <= temprature < 40:
    print("Its Hot")
elif 40 <= temprature:
    print("Its Very Hot")
else:
    print("Invalid Input")