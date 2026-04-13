wind_speed = int(input("Enter the wind speed of the storm in miles per hour: "))
if wind_speed >= 157:
    print("The storm is a Category 5 hurricane.")
elif wind_speed >= 130:
    print("The storm is a Category 4 hurricane.")
elif wind_speed >= 111:
    print("The storm is a Category 3 hurricane.")
elif wind_speed >= 96:
    print("The storm is a Category 2 hurricane.")
elif wind_speed >= 74:
    print("The storm is a Category 1 hurricane.")
else:
    print("The storm is a tropical storm.")