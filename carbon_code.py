import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# --- User Inputs ---
name = "Waithira"
country = "United States"
household_size = 2

# Estimates (kg CO2 / month)
transport = 0
electricity = 900 * 0.45    # 900 kWh, natural gas factor
food = 8 * 30               # average meat eater
shopping = 10 * 15          # 10 fashion items

# --- Data ---
df = pd.DataFrame({
    "Category": ["Transport", "Electricity", "Food", "Shopping"],
    "Emissions": [transport, electricity, food, shopping]
})

# Totals
total_monthly = df["Emissions"].sum()
total_annual = total_monthly * 12
per_capita = total_annual / household_size
avg_us = 16000  # kg CO₂ per year
difference = abs(total_annual - avg_us)
comparison = "Below" if total_annual < avg_us else "Above"

# --- Create Figure ---
fig = plt.figure(figsize=(14,8))
gs = fig.add_gridspec(2, 2, height_ratios=[1,2])

# Report Text Section
ax0 = fig.add_subplot(gs[0, :])
ax0.axis("off")

report_text = f"""
CARBON FOOTPRINT ANALYSIS REPORT

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}

User: **{name}**
Country: **{country}**
Household Size: **{household_size}**

Monthly Breakdown (kg CO₂)
Transport   : {transport:.1f}
Electricity : {electricity:.1f}
Food        : {food:.1f}
Shopping    : {shopping:.1f}

**Total Monthly**: {total_monthly:.1f} kg CO₂
**Annual Total** : {total_annual:.1f} kg CO₂ ({total_annual/1000:.1f} tons)

**Per Capita**   : {per_capita:.1f} kg CO₂/year
**Benchmark**    : Average US footprint = {avg_us/1000:.1f} tons/year
**Comparison**   : {comparison} the US average by {difference:,.0f} kg
"""
ax0.text(0, 0.9, report_text, fontsize=12, va="top", ha="left", family="monospace")

# Pie Chart
ax1 = fig.add_subplot(gs[1,0])
ax1.pie(df["Emissions"], labels=df["Category"], autopct='%1.1f%%',
        colors=["#4F81BD","#9BBB59","#C0504D","#8064A2"], startangle=90)
ax1.set_title("Proportional Breakdown", fontsize=12, fontweight="bold")

# Bar Chart
ax2 = fig.add_subplot(gs[1,1])
bars = ax2.bar(df["Category"], df["Emissions"], color="#4F81BD")
ax2.axhline(y=avg_us/12, color="red", linestyle="--", label="US Avg (monthly)")
ax2.set_title("Monthly Emissions by Category", fontsize=12, fontweight="bold")
ax2.set_ylabel("kg CO₂")
ax2.legend()

for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height+10,
             f'{height:.0f}', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("footprint_dashboard.png") 
plt.show()
