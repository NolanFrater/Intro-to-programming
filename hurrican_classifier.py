def classify_hurricane(wind_speed):
    try:
        input_value = int(input("Enter the wind speed of the storm in miles per hour: "))
        wind_speed = int(input_value)
        if wind_speed >= 157:
            return "The storm is a Category 5 hurricane."
        elif wind_speed >= 130:
            return "The storm is a Category 4 hurricane."
        elif wind_speed >= 111:
             return "The storm is a Category 3 hurricane."
        elif wind_speed >= 96:
             return "The storm is a Category 2 hurricane."
        elif wind_speed >= 74:
            return "The storm is a Category 1 hurricane."
        else:
            return "The storm is a tropical storm."
    except ValueError:
        return "Invalid input. Please enter a numeric value."

print(classify_hurricane(0))

