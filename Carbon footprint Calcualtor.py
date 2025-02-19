# Carbon Footprint Calculator

## Description
This script calculates your estimated monthly carbon footprint based on your travel, electricity usage, and food consumption.

## How to Use
1. Run the script using Python.
2. Enter your daily travel distance and transport type.
3. Provide your daily electricity usage.
4. Estimate your daily food-based carbon footprint.
5. View the calculated monthly carbon footprint and a graphical breakdown.

## Dependencies
- Python 3.x
- Matplotlib (`pip install matplotlib`)

## Running the Script
Execute the script using:
```sh
python script_name.py
```

---

import matplotlib.pyplot as plt

def get_float_input(prompt):
    """Helper function to get a valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_int_input(prompt, valid_options):
    """Helper function to get a valid integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
    
    print("Invalid transport option. Defaulting to 0 emissions.")
    return 0

def plot_results(categories, values):
    """Generates a bar chart for carbon footprint distribution."""
    plt.bar(categories, values, color=['blue', 'red', 'green'])
    plt.xlabel("Categories")
    plt.ylabel("Carbon Footprint (kg CO₂)")
    plt.title("Your Carbon Footprint Breakdown")
    plt.show()

def main():
    print("Welcome to the Carbon Footprint Calculator!")
    carbon_transport = travel()
    
    carbon_electricity = get_float_input("Enter your daily electricity usage in kWh: ") * 0.4 * 30
    carbon_food = get_float_input("Enter your daily food-based carbon footprint (estimate in kg CO₂): ") * 30
    
    total_footprint = carbon_transport + carbon_electricity + carbon_food
    print(f"\nYour monthly carbon footprint is {total_footprint:.2f} kg CO₂.")
    
    plot_results(["Transport", "Electricity", "Food"], [carbon_transport, carbon_electricity, carbon_food])

if __name__ == "__main__":
    main()