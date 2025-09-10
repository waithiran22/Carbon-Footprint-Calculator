# Program to calculate a user's carbon footprint based on daily activities

# Initialize global variables to store carbon footprints
carbon_transport = 0
carbon_electricity = 0
carbon_food = 0

def introduction():
    """
    Prints an introduction to the carbon footprint calculator,
    explaining the average carbon footprint and the purpose of the program.
    """
    print("The average carbon footprint of an American is about 16 tons of CO₂ emissions per year. "
          "This is one of the highest per capita rates in the world, largely due to high energy consumption, "
          "reliance on fossil fuels, and consumer habits.")
    print("This program will help you calculate your day-to-day carbon footprint and provide suggestions to reduce it.")
    print("Let's get started!\n")
    # Start with travel calculation
    travel()

def travel():
    """
    Calculates carbon footprint based on daily travel.
    Asks the user for daily distance traveled and type of transportation,
    then calculates the monthly CO₂ emissions for that mode of transport.
    """
    global carbon_transport  # Access global variable
    try:
        distance_daily = float(input("How long is your daily travel in kilometers: "))
        distance_monthly = distance_daily * 30  # Assumes 30 days of travel in a month
    except ValueError:
        print("Please enter a valid distance.")
        return  # Exit function if input is invalid

    print("Transportation types:\n  1) Car \n  2) Public transportation\n  3) Biking\n  4) Walking\n  5) Airplane")
    try:
        transport_type = int(input("Pick the type of transportation you used the most in the last month (1-5): "))
    except ValueError:
        print("Please enter a valid number for the transportation type.")
        return  # Exit function if input is invalid

    # Car transportation options
    if transport_type == 1:
        fuel = input("Do you use petrol, diesel, or electric cars? ").lower()
        if fuel == "diesel":
            carbon_transport = 0.28 * distance_monthly  # Diesel: 0.28 kg CO₂ per km
        elif fuel == "petrol":
            carbon_transport = 0.24 * distance_monthly  # Petrol: 0.24 kg CO₂ per km
        elif fuel == "electric":
            carbon_transport = 0.03 * distance_monthly  # Electric: 0.03 kg CO₂ per km
        else:
            print("Invalid fuel type entered.")

    # Public transportation options
    elif transport_type == 2:
        public_transport = input("Do you use the bus, train, or subway? ").lower()
        if public_transport == "bus":
            carbon_transport = 0.1 * distance_monthly  # Bus: 0.1 kg CO₂ per km
        elif public_transport == "train":
            carbon_transport = 0.05 * distance_monthly  # Train: 0.05 kg CO₂ per km
        elif public_transport == "subway":
            carbon_transport = 0.03 * distance_monthly  # Subway: 0.03 kg CO₂ per km
        else:
            print("Invalid public transport option entered.")

    # Biking and walking have zero carbon emissions
    elif transport_type in [3, 4]:
        carbon_transport = 0  # No CO₂ emissions for biking or walking

    # Airplane travel
    elif transport_type == 5:
        air_travel = input("Was the flight short (<2 hours), medium (2-5 hours), or long (>8 hours)? ").lower()
        if air_travel == "short":
            carbon_transport = 0.25 * distance_monthly  # Short flight: 0.25 kg CO₂ per km
        elif air_travel == "medium":
            carbon_transport = 0.45 * distance_monthly  # Medium flight: 0.45 kg CO₂ per km
        elif air_travel == "long":
            carbon_transport = 0.6 * distance_monthly  # Long flight: 0.6 kg CO₂ per km
        else:
            print("Invalid flight type entered.")

    # Output the calculated carbon footprint for travel
    print(f"\nYour carbon footprint from travel is: {carbon_transport:.2f} kg CO₂ per month")
    print("Let's move on to your electricity consumption.\n")
    # Proceed to electricity calculation
    electricity()

def electricity():
    """
    Calculates carbon footprint based on electricity consumption.
    Asks the user to choose the energy source used the most,
    then calculates the monthly CO₂ emissions based on the energy source.
    """
    global carbon_electricity  # Access global variable
    print("Energy usage types:\n  1) Coal \n  2) Natural gas\n  3) Grid average\n  4) Renewables")
    try:
        energy_type = int(input("Pick the type of energy you used the most in the last month (1-4): "))
    except ValueError:
        print("Please enter a valid number for the energy type.")
        return  # Exit function if input is invalid

    # CO₂ emissions per kWh for different energy sources (in kg CO₂ per kWh)
    hours_per_day = 24
    if energy_type == 1:  # Coal
        carbon_electricity = 0.91 * hours_per_day  # Coal: 0.91 kg CO₂ per kWh
    elif energy_type == 2:  # Natural gas
        carbon_electricity = 0.45 * hours_per_day  # Natural gas: 0.45 kg CO₂ per kWh
    elif energy_type == 3:  # Grid average (mixed energy sources)
        carbon_electricity = 0.45 * hours_per_day  # Grid average: 0.4-0.5 kg CO₂ per kWh
    elif energy_type == 4:  # Renewables
        type_renewable = int(input("Pick your renewable energy type: 1) Wind 2) Solar 3) Hydroelectric: "))
        if type_renewable == 1:
            carbon_electricity = 0.015 * hours_per_day  # Wind: 0.01-0.02 kg CO₂ per kWh
        elif type_renewable == 2:
            carbon_electricity = 0.045 * hours_per_day  # Solar: 0.03-0.06 kg CO₂ per kWh
        elif type_renewable == 3:
            carbon_electricity = 0.02 * hours_per_day  # Hydroelectric: 0.01-0.03 kg CO₂ per kWh
        else:
            print("Invalid renewable energy type entered.")
            return

    # Output the calculated carbon footprint for electricity
    print(f"\nYour carbon footprint from electricity is: {carbon_electricity:.2f} kg CO₂ per day")
    print("Let's move on to your food and diet.\n")
    # Proceed to food calculation
    food()

def food():
    """
    Calculates carbon footprint based on food consumption.
    Asks the user how many servings of each food category they consume daily,
    then calculates the daily CO₂ emissions for that food consumption.
    """
    global carbon_food  # Access global variable
    print("Now we will calculate your carbon footprint from your food consumption.\n")

    # Food categories and their average carbon footprint in kg CO₂ per serving
    food_categories = {
        "Beef": 27, "Lamb": 39.2, "Chicken": 6.9, "Pork": 12.1, "Fish": 5.4,
        "Eggs": 4.8, "Cheese": 13.5, "Milk": 1.9, "Vegetables": 2.0, "Fruits": 1.1
    }

    total_carbon_footprint = 0  # Initialize total carbon footprint for food

    # Iterate over each food category and ask for servings per day
    for food_item, footprint_per_serving in food_categories.items():
        try:
            servings = float(input(f"How many servings of {food_item} do you consume per day? "))
            total_carbon_footprint += servings * footprint_per_serving  # Add to total footprint
        except ValueError:
            print("Please enter a valid number for servings.")

    # Store the total carbon footprint for food
    carbon_food = total_carbon_footprint

    # Output the total carbon footprint from food consumption
    print(f"\nYour total carbon footprint from food consumption is: {carbon_food:.2f} kg CO₂ per day\n")
    # Proceed to total footprint calculation
    calculate_total_footprint()

def calculate_total_footprint():
    """
    Calculates the total carbon footprint based on travel, electricity, and food,
    and compares it to the average annual carbon footprint of an American (16 tons).
    """
    # Convert daily and monthly footprints to annual footprints
    total_annual_carbon = (carbon_transport * 12) + (carbon_electricity * 365) + (carbon_food * 365)

    print(f"\nYour total annual carbon footprint is: {total_annual_carbon:.2f} kg CO₂ per year")

    # Compare to the average American footprint (16,000 kg CO₂ per year)
    if total_annual_carbon > 16000:
        print("Your carbon footprint is above the average for Americans (16 tons per year).")
    else:
        print("Your carbon footprint is below the average for Americans (16 tons per year).")

# Start the program
introduction()
