# define conversion functions

def volume_converter(volume_value, conversion_direction):
    if conversion_direction == "liters  to gallons":
        gallons_value = volume_value / 3.785411784
        return gallons_value
    elif conversion_direction == "liters to cups":
        yards_value = volume_value * 4.2267528377
        return yards_value
    elif conversion_direction == "gallons to liters":
        liters_value = volume_value * 3.785411784
        return liters_value
    elif conversion_direction == "cups to liters":
        liters_value = volume_value / 4.2267528377
        return liters_value
    elif conversion_direction == "ounces to liters":
        liters_value = volume_value / 33.8140227018
        return liters_value
    elif conversion_direction == "liters to ounces":
        ounces_value = volume_value * 33.8140227018
        return ounces_value
    elif conversion_direction == "liters to cubic meters":
        days_value = volume_value / 1000
        return days_value
    elif conversion_direction == "cubic meters to liters":
        seconds_value = volume_value * 1000
        return seconds_value


# main program loop

print("Welcome to the conversion calculator!\n")

while True:
    category = input("Choose a category:\n1. LENGTH\n2. MASS AND WEIGHT\n3. VOLUME\n4. SPEED\n5. TIME\n6. QUIT\n")
    if category == '6':
        break
    elif category == '3':
        conversion_direction = input("Choose a conversion direction:\n1. liters  to gallons\n2. liters to cups\n"
                                     "3. gallons to liters\n4. cups to liters\n5. ounces to liters\n"
                                     "6. liters to ounces\n7. liters to cubic meters\n8. cubic meters to liters\n")
        volume_value = float(input("Enter the volume value: "))
        if conversion_direction == '1':
            converted_value = volume_converter(volume_value, "liters  to gallons")
            print(f"{volume_value} liters is {converted_value} gallons.\n")
        elif conversion_direction == '2':
            converted_value = volume_converter(volume_value, "liters to cups")
            print(f"{volume_value} liters is {converted_value} cups.\n")
        elif conversion_direction == '3':
            converted_value = volume_converter(volume_value, "gallons to liters")
            print(f"{volume_value} gallons is {converted_value} liters.\n")
        elif conversion_direction == '4':
            converted_value = volume_converter(volume_value, "cups to liters")
            print(f"{volume_value} cups is {converted_value} liters.\n")
        elif conversion_direction == '5':
            converted_value = volume_converter(volume_value, "ounces to liters")
            print(f"{volume_value} ounces is {converted_value} liters.\n")
        elif conversion_direction == '6':
            converted_value = volume_converter(volume_value, "liters to ounces")
            print(f"{volume_value} liters is {converted_value} ounces.\n")
        elif conversion_direction == '7':
            converted_value = volume_converter(volume_value, "liters to cubic meters")
            print(f"{volume_value} second is {converted_value} days.\n")
        elif conversion_direction == '8':
            converted_value = volume_converter(volume_value, "cubic meters to liters")
            print(f"{volume_value} days is {converted_value} seconds.\n")
    elif category == '2':
        print("This feature is coming soon!\n")
    else:
        print("Invalid input, please try again.\n")
