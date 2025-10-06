import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import json
import os

class CarbonFootprintCalculator:
    def __init__(self):
        self.footprints = {
            'transport': 0,
            'electricity': 0,
            'food': 0,
            'shopping': 0
        }
        self.user_data = {}
        self.history = []
        
        self.emission_factors = {
            'transport': {
                'car_petrol': 0.24,
                'car_diesel': 0.28,
                'car_electric': 0.03,
                'bus': 0.1,
                'train': 0.05,
                'subway': 0.03,
                'motorcycle': 0.15,
                'short_flight': 0.25,
                'medium_flight': 0.45,
                'long_flight': 0.6,
                'biking': 0,
                'walking': 0
            },
            'electricity': {
                'coal': 0.91,
                'natural_gas': 0.45,
                'grid_average': 0.45,
                'wind': 0.015,
                'solar': 0.045,
                'hydro': 0.02,
                'nuclear': 0.012
            },
            'food': {
                'beef': 27, 'lamb': 39.2, 'chicken': 6.9, 'pork': 12.1,
                'fish': 5.4, 'eggs': 4.8, 'cheese': 13.5, 'milk': 1.9,
                'vegetables': 2.0, 'fruits': 1.1, 'grains': 1.4, 'nuts': 0.3
            },
            'shopping': {
                'fast_fashion': 15,  
                'electronics': 50,  
                'furniture': 100,    
                'plastic_bottles': 0.2  
            }
        }

    def introduction(self):
        """Enhanced introduction with visual elements"""
        print("🌍" * 50)
        print("          CARBON FOOTPRINT CALCULATOR PRO")
        print("🌍" * 50)
        print("\n📊 The average American carbon footprint is about 16 tons of CO₂ per year.")
        print("💡 This calculator helps you understand and reduce your environmental impact.")
        print("🌟 New features: Historical tracking, personalized tips, and visual analytics!\n")
        
        self.get_user_info()
        self.main_menu()

    def get_user_info(self):
        """Collect basic user information for personalization"""
        print("👤 Let's get to know you better!")
        self.user_data['name'] = input("What's your name? ").strip()
        self.user_data['country'] = input("Which country do you live in? ").strip()
        self.user_data['household_size'] = self.get_positive_number("How many people in your household? ")
        
        print(f"\nWelcome, {self.user_data['name']}! Let's calculate your carbon footprint. 🌱")

    def main_menu(self):
        """Interactive main menu for different calculator sections"""
        while True:
            print("\n" + "="*60)
            print("🏠 MAIN MENU")
            print("="*60)
            print("1. 🚗 Calculate Transport Footprint")
            print("2. 💡 Calculate Electricity Footprint") 
            print("3. 🍎 Calculate Food Footprint")
            print("4. 🛍️ Calculate Shopping Footprint")
            print("5. 📊 View Complete Analysis")
            print("6. 📈 View Historical Data")
            print("7. 💡 Get Personalized Recommendations")
            print("8. 💾 Save Current Calculation")
            print("9. 🚪 Exit")
            
            choice = input("\nChoose an option (1-9): ").strip()
            
            if choice == '1':
                self.calculate_transport()
            elif choice == '2':
                self.calculate_electricity()
            elif choice == '3':
                self.calculate_food()
            elif choice == '4':
                self.calculate_shopping()
            elif choice == '5':
                self.show_complete_analysis()
            elif choice == '6':
                self.show_history()
            elif choice == '7':
                self.show_recommendations()
            elif choice == '8':
                self.save_calculation()
            elif choice == '9':
                print(f"\nThank you for using the calculator, {self.user_data['name']}! 🌍")
                break
            else:
                print("❌ Invalid choice. Please try again.")

    def calculate_transport(self):
        """Enhanced transport calculation with multiple vehicle support"""
        print("\n" + "🚗" * 20)
        print("      TRANSPORTATION CALCULATOR")
        print("🚗" * 20)
        
        total_transport = 0
        vehicles = []
        
        while True:
            print("\nVehicle types:")
            transport_options = [
                "1. Car (Petrol)", "2. Car (Diesel)", "3. Car (Electric)",
                "4. Bus", "5. Train", "6. Subway", "7. Motorcycle",
                "8. Bicycle", "9. Walking", "10. Airplane"
            ]
            for option in transport_options:
                print(f"   {option}")
            
            try:
                choice = int(input("\nSelect vehicle type (0 to finish): "))
                if choice == 0:
                    break
                
                vehicle_data = self.get_vehicle_data(choice)
                if vehicle_data:
                    vehicles.append(vehicle_data)
                    total_transport += vehicle_data['emissions']
                    
            except ValueError:
                print("❌ Please enter a valid number.")
        
        self.footprints['transport'] = total_transport
        print(f"\n✅ Total transport emissions: {total_transport:.2f} kg CO₂ per month")
        self.show_transport_breakdown(vehicles)

    def get_vehicle_data(self, choice):
        """Get data for a specific vehicle type"""
        vehicle_map = {
            1: ('car_petrol', 'Petrol Car'),
            2: ('car_diesel', 'Diesel Car'),
            3: ('car_electric', 'Electric Car'),
            4: ('bus', 'Bus'),
            5: ('train', 'Train'),
            6: ('subway', 'Subway'),
            7: ('motorcycle', 'Motorcycle'),
            8: ('biking', 'Bicycle'),
            9: ('walking', 'Walking'),
            10: ('airplane', 'Airplane')
        }
        
        if choice not in vehicle_map:
            print("❌ Invalid vehicle type")
            return None
            
        vehicle_key, vehicle_name = vehicle_map[choice]
        
        if choice == 10:  # Airplane
            flight_type = input("Flight type (short/medium/long): ").lower()
            distance = self.get_positive_number("Distance traveled (km): ")
            factor_key = f"{flight_type}_flight"
        else:
            distance = self.get_positive_number(f"Daily distance for {vehicle_name} (km): ")
            factor_key = vehicle_key
        
        monthly_distance = distance * 30
        emissions = monthly_distance * self.emission_factors['transport'].get(factor_key, 0)
        
        return {
            'name': vehicle_name,
            'distance': monthly_distance,
            'emissions': emissions
        }

    def calculate_electricity(self):
        """Enhanced electricity calculation with appliance breakdown"""
        print("\n" + "💡" * 20)
        print("      ELECTRICITY CALCULATOR")
        print("💡" * 20)
        
        # Energy source
        print("\nEnergy sources:")
        energy_sources = ["1. Coal", "2. Natural Gas", "3. Grid Average", 
                         "4. Wind", "5. Solar", "6. Hydro", "7. Nuclear"]
        for source in energy_sources:
            print(f"   {source}")
        
        try:
            energy_choice = int(input("\nSelect energy source (1-7): "))
            energy_keys = ['coal', 'natural_gas', 'grid_average', 'wind', 'solar', 'hydro', 'nuclear']
            if 1 <= energy_choice <= 7:
                energy_key = energy_keys[energy_choice - 1]
                energy_factor = self.emission_factors['electricity'][energy_key]
            else:
                print("❌ Invalid choice, using grid average")
                energy_factor = self.emission_factors['electricity']['grid_average']
        except ValueError:
            print("❌ Invalid input, using grid average")
            energy_factor = self.emission_factors['electricity']['grid_average']
        
        # Appliance usage
        print("\n💡 Common household appliances:")
        appliances = {
            'Refrigerator': (150, 24),
            'Air Conditioner': (1500, 8),
            'Heating': (2000, 6),
            'Lighting': (60, 5),
            'TV': (100, 4),
            'Computer': (150, 6),
            'Washing Machine': (500, 1),
            'Dishwasher': (1200, 1)
        }
        
        total_kwh = 0
        for appliance, (watts, hours) in appliances.items():
            use = input(f"Hours per day for {appliance} ({watts}W): ").strip()
            if use:
                try:
                    hours_used = float(use)
                    daily_kwh = (watts / 1000) * hours_used
                    total_kwh += daily_kwh
                except ValueError:
                    continue
        
        monthly_emissions = total_kwh * 30 * energy_factor
        self.footprints['electricity'] = monthly_emissions
        
        print(f"\n✅ Total electricity emissions: {monthly_emissions:.2f} kg CO₂ per month")
        print(f"📊 Estimated monthly consumption: {total_kwh * 30:.1f} kWh")

    def calculate_food(self):
        """Enhanced food calculator with diet type detection"""
        print("\n" + "🍎" * 20)
        print("      FOOD CALCULATOR")
        print("🍎" * 20)
        
        print("\n🍽️  First, let's understand your diet type:")
        print("   1. Heavy meat eater (meat 2+ times daily)")
        print("   2. Average meat eater (meat daily)")
        print("   3. Vegetarian (no meat, but dairy/eggs)")
        print("   4. Vegan (no animal products)")
        print("   5. Custom (calculate specific items)")
        
        try:
            diet_choice = int(input("\nSelect your diet type (1-5): "))
        except ValueError:
            diet_choice = 5
        
        if diet_choice == 5:
            # Custom calculation
            total_food = 0
            for food, factor in self.emission_factors['food'].items():
                try:
                    servings = float(input(f"Servings of {food} per day: "))
                    total_food += servings * factor
                except ValueError:
                    continue
        else:
            # Estimate based on diet type
            diet_estimates = {1: 12, 2: 8, 3: 5, 4: 3}  # kg CO₂ per day
            total_food = diet_estimates.get(diet_choice, 6)
            print(f"📊 Estimated food emissions: {total_food} kg CO₂ per day")
        
        self.footprints['food'] = total_food * 30  # Monthly
        print(f"\n✅ Total food emissions: {self.footprints['food']:.2f} kg CO₂ per month")

    def calculate_shopping(self):
        """New shopping footprint calculator"""
        print("\n" + "🛍️" * 20)
        print("      SHOPPING CALCULATOR")
        print("🛍️" * 20)
        
        total_shopping = 0
        print("\n🛒 How many of these items do you buy per month:")
        
        for item, factor in self.emission_factors['shopping'].items():
            try:
                quantity = float(input(f"   {item.replace('_', ' ').title()}: "))
                total_shopping += quantity * factor
            except ValueError:
                continue
        
        self.footprints['shopping'] = total_shopping
        print(f"\n✅ Total shopping emissions: {total_shopping:.2f} kg CO₂ per month")

    def show_complete_analysis(self):
        """Comprehensive analysis with visualizations"""
        total_monthly = sum(self.footprints.values())
        total_annual = total_monthly * 12
        
        print("\n" + "📊" * 20)
        print("      COMPLETE CARBON ANALYSIS")
        print("📊" * 20)
        
        print(f"\n👤 User: {self.user_data['name']}")
        print(f"🏠 Household Size: {self.user_data['household_size']}")
        print(f"📅 Calculation Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        print("\n" + "─" * 50)
        print("MONTHLY BREAKDOWN (kg CO₂):")
        print("─" * 50)
        for category, value in self.footprints.items():
            percentage = (value / total_monthly * 100) if total_monthly > 0 else 0
            print(f"   {category.title():<12}: {value:>8.2f} kg ({percentage:>5.1f}%)")
        
        print("─" * 50)
        print(f"   {'TOTAL':<12}: {total_monthly:>8.2f} kg")
        
        print(f"\n📈 ANNUAL TOTAL: {total_annual:,.2f} kg CO₂ ({total_annual/1000:.1f} tons)")
        
        # Comparison
        avg_american = 16000  
        comparison = "above" if total_annual > avg_american else "below"
        difference = abs(total_annual - avg_american)
        print(f"🌎 Your footprint is {difference:,.0f} kg {comparison} the average American")
        
        # Per capita
        per_capita = total_annual / self.user_data['household_size']
        print(f"👥 Per capita: {per_capita:,.0f} kg per person per year")
        
        self.create_visualizations()

    def create_visualizations(self):
        """Create visual charts of the carbon footprint"""
        try:
            # Pie chart
            labels = [f'{k.title()}\n({v:.1f} kg)' for k, v in self.footprints.items() if v > 0]
            sizes = [v for v in self.footprints.values() if v > 0]
            colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
            
            plt.figure(figsize=(12, 4))
            
            plt.subplot(1, 2, 1)
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.title('Monthly Carbon Footprint Breakdown')
            
            # Bar chart
            plt.subplot(1, 2, 2)
            categories = [k.title() for k, v in self.footprints.items() if v > 0]
            values = [v for v in self.footprints.values() if v > 0]
            
            bars = plt.bar(categories, values, color=colors[:len(categories)])
            plt.title('Monthly Emissions by Category')
            plt.ylabel('kg CO₂')
            plt.xticks(rotation=45)
            
            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.1f} kg',
                        ha='center', va='bottom')
            
            plt.tight_layout()
            plt.show()
            
        except ImportError:
            print("\n📊 (Visualization requires matplotlib - install with: pip install matplotlib)")

    def show_recommendations(self):
        """Personalized recommendations based on footprint"""
        print("\n" + "💡" * 20)
        print("      PERSONALIZED RECOMMENDATIONS")
        print("💡" * 20)
        
        highest_category = max(self.footprints.items(), key=lambda x: x[1])
        category, value = highest_category
        
        print(f"\n🎯 Your highest emissions come from: {category.title()} ({value:.1f} kg/month)")
        print("\n🌱 Recommendations to reduce your footprint:")
        
        recommendations = {
            'transport': [
                "🚗 Use public transportation 2+ days per week",
                "🚲 Try biking or walking for short trips",
                "🚗 Carpool with colleagues or neighbors",
                "✈️ Limit air travel when possible",
                "🔌 Consider an electric vehicle for your next car"
            ],
            'electricity': [
                "💡 Switch to LED bulbs",
                "🌞 Use natural light during daytime",
                "🔌 Unplug devices when not in use",
                "🏠 Improve home insulation",
                "☀️ Consider solar panels if feasible"
            ],
            'food': [
                "🍔 Reduce red meat consumption",
                "🥦 Incorporate more plant-based meals",
                "🏷️ Buy local and seasonal produce",
                "🗑️ Reduce food waste with meal planning",
                "🌱 Try meatless Mondays"
            ],
            'shopping': [
                "🛍️ Buy secondhand when possible",
                "📱 Keep electronics longer",
                "🚫 Avoid fast fashion",
                "💧 Use reusable water bottles",
                "🛒 Choose products with less packaging"
            ]
        }
        
        for rec in recommendations.get(category, []):
            print(f"   • {rec}")
        
        print("\n🌟 Additional general tips:")
        general_tips = [
            "📊 Track your footprint monthly",
            "🌳 Support carbon offset projects",
            "🏠 Conduct a home energy audit",
            "🚰 Reduce water consumption",
            "🌎 Advocate for climate policies"
        ]
        for tip in general_tips:
            print(f"   • {tip}")

    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("\n📝 No previous calculations found.")
            return
        
        print("\n" + "📈" * 20)
        print("      CALCULATION HISTORY")
        print("📈" * 20)
        
        for i, calc in enumerate(self.history[-5:], 1):  # Show last 5
            print(f"\n{i}. {calc['date']} - Total: {calc['total']:.1f} kg CO₂/month")

    def save_calculation(self):
        """Save current calculation to history"""
        calculation = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'footprints': self.footprints.copy(),
            'total': sum(self.footprints.values()),
            'user_data': self.user_data.copy()
        }
        self.history.append(calculation)
        print(f"\n💾 Calculation saved on {calculation['date']}")

    def show_transport_breakdown(self, vehicles):
        """Show detailed transport breakdown"""
        if not vehicles:
            return
        
        print("\n🚗 TRANSPORT BREAKDOWN:")
        print("─" * 40)
        for vehicle in vehicles:
            print(f"   {vehicle['name']:<15}: {vehicle['emissions']:>6.1f} kg CO₂")
        print("─" * 40)

    def get_positive_number(self, prompt):
        """Utility function to get positive numbers from user"""
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("❌ Please enter a positive number")
            except ValueError:
                print("❌ Please enter a valid number")

if __name__ == "__main__":
    calculator = CarbonFootprintCalculator()
    calculator.introduction()

