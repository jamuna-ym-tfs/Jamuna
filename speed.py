# define conversion functions

def speed_converter(speed_value, conversion_direction):
    if conversion_direction == "mph to kph":
        kph_value = speed_value * 1.609344
        return kph_value
    elif conversion_direction == "meters per second  to miles per hour":
        miles_per_hour_value = speed_value * 2.2369362921
        return miles_per_hour_value
    elif conversion_direction == "kph to mph":
        mph_value = speed_value / 1.609344
        return mph_value
    elif conversion_direction == "miles per hour to meters per second":
        meters_per_second_value = speed_value / 2.2369362921
        return meters_per_second_value
    elif conversion_direction == "knot to mph":
        mph_value = speed_value * 1.150779448
        return mph_value
    elif conversion_direction == "mph to knot":
        knot_value = speed_value / 1.150779448
        return knot_value
    elif conversion_direction == "feet per second to mph":
        mph_value = speed_value / 1.4666666667
        return mph_value
    elif conversion_direction == "mph to feet per second":
        feet_per_second_value = speed_value * 1.4666666667
        return feet_per_second_value


# main program loop

print("Welcome to the conversion calculator!\n")

while True:
    category = input("Choose a category:\n1. LENGTH\n2. MASS AND WEIGHT\n3. VOLUME\n4. SPEED\n5. TIME\n6. QUIT\n")
    if category == '6':
        break
    elif category == '4':
        conversion_direction = input("Choose a conversion direction:\n1. mph to kph\n"
                                     "2. meters per second  to miles per hour\n3. kph to mph"
                                     "\n4. miles per hour to meters per second\n5. knot to mph\n6. mph to knot"
                                     "\n7. feet per second to mph\n8. mph to feet per second\n")
        speed_value = float(input("Enter the speed value: "))
        if conversion_direction == '1':
            converted_value = speed_converter(speed_value, "mph to kph")
            print(f"{speed_value} mph is {converted_value} kph.\n")
        elif conversion_direction == '2':
            converted_value = speed_converter(speed_value, "meters per second  to miles per hour")
            print(f"{speed_value} meters per second is {converted_value} miles per hour.\n")
        elif conversion_direction == '3':
            converted_value = speed_converter(speed_value, "kph to mph")
            print(f"{speed_value} kph is {converted_value} mph.\n")
        elif conversion_direction == '4':
            converted_value = speed_converter(speed_value, "miles per hour to meters per second")
            print(f"{speed_value} miles per hour is {converted_value} meters per second.\n")
        elif conversion_direction == '5':
            converted_value = speed_converter(speed_value, "knot to mph")
            print(f"{speed_value} knot is {converted_value} mph.\n")
        elif conversion_direction == '6':
            converted_value = speed_converter(speed_value, "mph to knot")
            print(f"{speed_value} mph is {converted_value} knot.\n")
        elif conversion_direction == '7':
            converted_value = speed_converter(speed_value, "feet per second to mph")
            print(f"{speed_value} feet per second is {converted_value} mph.\n")
        elif conversion_direction == '8':
            converted_value = speed_converter(speed_value, "mph to feet per second")
            print(f"{speed_value} mph is {converted_value} feet per second.\n")
    elif category == '2':
        print("This feature is coming soon!\n")
    else:
        print("Invalid input, please try again.\n")
