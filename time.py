# define conversion functions

def time_converter(time_value, conversion_direction):
    if conversion_direction == "days to minutes":
        minutes_value = time_value * 1440
        return minutes_value
    elif conversion_direction == "hours  to seconds":
        seconds_value = time_value * 3600
        return seconds_value
    elif conversion_direction == "minutes to days":
        days_value = time_value / 1440
        return days_value
    elif conversion_direction == "seconds to hours":
        hours_value = time_value / 3600
        return hours_value
    elif conversion_direction == "hours to days":
        days_value = time_value / 24
        return days_value
    elif conversion_direction == "days to hours":
        hours_value = time_value * 24
        return hours_value
    elif conversion_direction == "seconds to days":
        days_value = time_value / 86400
        return days_value
    elif conversion_direction == "days to seconds":
        seconds_value = time_value * 86400
        return seconds_value


# main program loop

print("Welcome to the conversion calculator!\n")

while True:
    category = input("Choose a category:\n1. LENGTH\n2. MASS AND WEIGHT\n3. VOLUME\n4. SPEED\n5. TIME\n6. QUIT\n")
    if category == '6':
        break
    elif category == '5':
        conversion_direction = input("Choose a conversion direction:\n1. days to minutes\n2. hours  to seconds\n"
                                     "3. minutes to days\n4. seconds to hours\n5. hours to days\n6. days to hours\n"
                                     "7. seconds to days\n8. days to seconds\n")
        time_value = float(input("Enter the time value: "))
        if conversion_direction == '1':
            converted_value = time_converter(time_value, "days to minutes")
            print(f"{time_value} days is {converted_value} minutes.\n")
        elif conversion_direction == '2':
            converted_value = time_converter(time_value, "hours  to seconds")
            print(f"{time_value} hours is {converted_value} yards.\n")
        elif conversion_direction == '3':
            converted_value = time_converter(time_value, "minutes to days")
            print(f"{time_value} minutes is {converted_value} days.\n")
        elif conversion_direction == '4':
            converted_value = time_converter(time_value, "seconds to hours")
            print(f"{time_value} seconds is {converted_value} hours.\n")
        elif conversion_direction == '5':
            converted_value = time_converter(time_value, "hours to days")
            print(f"{time_value} hours is {converted_value} days.\n")
        elif conversion_direction == '6':
            converted_value = time_converter(time_value, "days to hours")
            print(f"{time_value} days is {converted_value} hours.\n")
        elif conversion_direction == '7':
            converted_value = time_converter(time_value, "seconds to days")
            print(f"{time_value} seconds is {converted_value} days.\n")
        elif conversion_direction == '8':
            converted_value = time_converter(time_value, "days to seconds")
            print(f"{time_value} days is {converted_value} seconds.\n")
    elif category == '2':
        print("This feature is coming soon!\n")
    else:
        print("Invalid input, please try again.\n")
