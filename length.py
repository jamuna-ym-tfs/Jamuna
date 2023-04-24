# define conversion functions

def length_converter(length_value, conversion_direction):
    if conversion_direction == "Meters to Feet":
        feet_value = length_value * 3.28084
        return feet_value
    elif conversion_direction == "Meters to Yards":
        yards_value = length_value / 0.9144
        return yards_value
    elif conversion_direction == "Feet to Meters":
        meters_value = length_value / 3.28084
        return meters_value
    elif conversion_direction == "Yards to Meters":
        meters_value = length_value * 0.9144
        return meters_value
    elif conversion_direction == "Yards to Miles":
        miles_value = length_value / 1760.0
        return miles_value
    elif conversion_direction == "Miles to Yards":
        yards_value = length_value * 1760.0
        return yards_value
    elif conversion_direction == "Kilometers to Miles":
        miles_value = length_value / 1.60934
        return miles_value
    elif conversion_direction == "Miles to Kilometers":
        kilometers_value = length_value * 1.60934
        return kilometers_value


# main program loop

print("Welcome to the conversion calculator!\n")

while True:
    category = input("Choose a category:\n1. LENGTH\n2. MASS AND WEIGHT\n3. VOLUME\n4. SPEED\n5. TIME\n6. QUIT\n")
    if category == '6':
        break
    elif category == '1':
        conversion_direction = input("Choose a conversion direction:\n1. Meters to Feet\n2. Meters to Yards\n"
                                     "3. Feet to Meters\n4. Yards to Meters\n5. Yards to Miles\n6. Miles to Yards\n"
                                     "7. Kilometers to Miles\n8. Miles to Kilometers\n")
        length_value = float(input("Enter the length value: "))
        if conversion_direction == '1':
            converted_value = length_converter(length_value, "Meters to Feet")
            print(f"{length_value} Meters is {converted_value} Feet.\n")
        elif conversion_direction == '2':
            converted_value = length_converter(length_value, "Meters to Yards")
            print(f"{length_value} Meters is {converted_value} Yards.\n")
        elif conversion_direction == '3':
            converted_value = length_converter(length_value, "Feet to Meters")
            print(f"{length_value} Feet is {converted_value} Meters.\n")
        elif conversion_direction == '4':
            converted_value = length_converter(length_value, "Yards to Meters")
            print(f"{length_value} Yards is {converted_value} Meters.\n")
        elif conversion_direction == '5':
            converted_value = length_converter(length_value, "Yards to Miles")
            print(f"{length_value} Yards is {converted_value} Miles.\n")
        elif conversion_direction == '6':
            converted_value = length_converter(length_value, "Miles to Yards")
            print(f"{length_value} Miles is {converted_value} Yards.\n")
        elif conversion_direction == '7':
            converted_value = length_converter(length_value, "Kilometers to Miles")
            print(f"{length_value} Kilometers is {converted_value} Miles.\n")
        elif conversion_direction == '8':
            converted_value = length_converter(length_value, "Miles to Kilometers")
            print(f"{length_value} Miles is {converted_value} Kilometers.\n")
    elif category == '2':
        print("This feature is coming soon!\n")
    else:
        print("Invalid input, please try again..\n")

