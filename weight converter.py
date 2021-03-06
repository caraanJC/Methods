def convert_weight():
    try:
        weight = float(input("Weight: "))
        unit = input("lbs or kg? (L/K): ").upper()

        if unit == "L":
            multiplier = 0.453592
            symbol = "kg"
        elif unit == "K":
            multiplier = 2.20462
            symbol = "lbs"
        else:
            raise ValueError("Sorry, L or K only")

        weight = weight * multiplier

        return f"You are {weight} {symbol}"

    except ValueError:
        print("Please Enter appropriate values")


my_weight = convert_weight()

print(my_weight)
