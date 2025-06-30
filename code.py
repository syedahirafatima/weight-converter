# Weight Converter

print("Weight Converter")
print("1. Pounds to Kilograms")
print("2. Kilograms to Pounds")

choice = input("Enter 1 or 2 to choose conversion: ")

if choice == "1":
    pounds = float(input("Enter weight in pounds: "))
    kilograms = pounds * 0.453592
    print(pounds, "pounds is", round(kilograms, 2), "kilograms.")
    
elif choice == "2":
    kilograms = float(input("Enter weight in kilograms: "))
    pounds = kilograms / 0.453592
    print(kilograms, "kilograms is", round(pounds, 2), "pounds.")
    
else:
    print("Invalid choice. Please enter 1 or 2.")
