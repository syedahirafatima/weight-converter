# Weight Converter

print("Weight Converter")
print("1. Pounds to Kilograms")
print("2. Kilograms to Pounds")

choice = input("Enter 1 or 2 to choose conversion: ")

if choice == "1":
    pounds = float(input("Enter weight in pounds: "))
    kilograms = pounds * 0.453592
    print(f"{pounds} pounds is {kilograms:.2f} kilograms.")
    
elif choice == "2":
    kilograms = float(input("Enter weight in kilograms: "))
    pounds = kilograms / 0.453592
    print(f"{kilograms} kilograms is {pounds:.2f} pounds.")
    
else:
    print("Invalid choice. Please enter 1 or 2.")
