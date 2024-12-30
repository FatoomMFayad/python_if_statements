# Prompt the user to enter a temperature and either C for Celsius or F for Fahrenheit
degree = int(input("Enter the temperature: "))
temp_type = input("Enter  C for Celsius or F for Fahrenheit: ").strip().upper()
if temp_type == "C":
    degrees_f = (9*(degree /5) + 32 )
    print(f"{degree}°C is equal to {degrees_f:.2f}°F")
elif temp_type == "F":
    degrees_c = 5*(degree -32 )/9
    print(f"{degree}°F is equal to {degrees_c:.2f}°C")
else:
    print("Error: Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
