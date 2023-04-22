# define conversion functions

def mass_weight_converter(mass_weight_value, conversion_direction):
    if conversion_direction == "Kilograms to Pounds":
        pounds_weight = mass_weight_value * 2.2046226218
        return pounds_weight
    elif conversion_direction == "Grams to Ounces":
        ounces_weight = mass_weight_value / 28.349523125
        return ounces_weight
    elif conversion_direction == "Pounds to Kilograms":
        Kilograms_weight = mass_weight_value / 2.2046226218
        return Kilograms_weight
    elif conversion_direction == "Ounces to Grams":
        grams_weight = mass_weight_value * 28.349523125
        return grams_weight
    elif conversion_direction == "Pounds to Ounces":
        ounces_weight = mass_weight_value * 16.0
        return ounces_weight
    elif conversion_direction == "Ounces to Pounds":
        pounds_weight = mass_weight_value / 16
        return pounds_weight
    elif conversion_direction == "Grams to Pounds":
        miles_value = mass_weight_value / 453.59237
        return miles_value
    elif conversion_direction == "Pounds to Grams":
        grams_weight = mass_weight_value * 453.59237
        return grams_weight


while True:
    category = input("Choose a category:\n1. LENGTH\n2. MASS AND WEIGHT\n3. VOLUME\n4. SPEED\n5. TIME\n6. QUIT\n")
    if category == '6':
        break
    elif category == '2':
        conversion_direction = input("Choose a conversion direction:\n1. Kilograms to Pounds\n2. Grams to Ounces\n"
                                     "3. Pounds to Kilograms\n4. Ounces to Grams\n5. Pounds to Ounces\n"
                                     "6. Ounces to Pounds\n7. Grams to Pounds\n8. Pounds to Grams\n")
        mass_weight_value = float(input("Enter the Mass and Weight value: "))
        if conversion_direction == '1':
            converted_value = mass_weight_converter(mass_weight_value, "Kilograms to Pounds")
            print(f"{mass_weight_value} Kilograms is {converted_value} Pounds.\n")
        elif conversion_direction == '2':
            converted_value = mass_weight_converter(mass_weight_value, "Grams to Ounces")
            print(f"{mass_weight_value} Grams is {converted_value} Ounces.\n")
        elif conversion_direction == '3':
            converted_value = mass_weight_converter(mass_weight_value, "Pounds to Kilograms")
            print(f"{mass_weight_value} Pounds is {converted_value} Kilograms.\n")
        elif conversion_direction == '4':
            converted_value = mass_weight_converter(mass_weight_value, "Ounces to Grams")
            print(f"{mass_weight_value} Ounces is {converted_value} Grams.\n")
        elif conversion_direction == '5':
            converted_value = mass_weight_converter(mass_weight_value, "Pounds to Ounces")
            print(f"{mass_weight_value} Pounds is {converted_value} Ounces.\n")
        elif conversion_direction == '6':
            converted_value = mass_weight_converter(mass_weight_value, "Ounces to Pounds")
            print(f"{mass_weight_value} Ounces is {converted_value} Pounds.\n")
        elif conversion_direction == '7':
            converted_value = mass_weight_converter(mass_weight_value, "Grams to Pounds")
            print(f"{mass_weight_value} Grams is {converted_value} Pounds.\n")
        elif conversion_direction == '8':
            converted_value = mass_weight_converter(mass_weight_value, "Pounds to Grams")
            print(f"{mass_weight_value} Pounds is {converted_value} Grams.\n")
