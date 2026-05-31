# ==================================================
# CodeAlpha Data Science Internship
# Task 2: Unemployment Analysis with Python
# Author: Vansh Gupta
# ==================================================

# Import required libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# STEP 1: LOAD THE DATASET
# --------------------------------------------------

print("Loading Dataset...")

df = pd.read_csv("Unemployment in India.csv")

# Display first 5 rows

print("\nFirst 5 Rows:")
print(df.head())

# --------------------------------------------------
# STEP 2: DATA CLEANING
# --------------------------------------------------

# Some column names contain extra spaces.
# This removes unwanted spaces.

df.columns = df.columns.str.strip()

# Convert Date column into proper date format

df['Date'] = pd.to_datetime(
    df['Date'],
    dayfirst=True
)

# --------------------------------------------------
# STEP 3: DATA UNDERSTANDING
# --------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------------
# STEP 4: AVERAGE UNEMPLOYMENT OVER TIME
# --------------------------------------------------

print("\nCreating Unemployment Trend Graph...")

# Group data by date
# Then calculate average unemployment rate

monthly_rate = df.groupby(
    'Date'
)['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12,6))

monthly_rate.plot()

plt.title(
    "Average Unemployment Rate Over Time"
)

plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.grid(True)

plt.savefig("unemployment_trend.png")

plt.show()

# --------------------------------------------------
# LEARNING:
#
# groupby('Date')
# means:
#
# Combine all rows with same date
# and calculate average unemployment
# --------------------------------------------------

# --------------------------------------------------
# STEP 5: STATE-WISE UNEMPLOYMENT ANALYSIS
# --------------------------------------------------

print("\nCreating State-wise Analysis...")

state_rate = df.groupby(
    'Region'
)['Estimated Unemployment Rate (%)'].mean()

# Sort from highest to lowest

state_rate = state_rate.sort_values(
    ascending=False
)

plt.figure(figsize=(12,8))

sns.barplot(
    x=state_rate.values,
    y=state_rate.index
)

plt.title(
    "Average Unemployment Rate by State"
)

plt.xlabel("Unemployment Rate (%)")
plt.ylabel("State")

plt.savefig("state_unemployment.png")

plt.show()

# --------------------------------------------------
# LEARNING:
#
# Which states had the highest unemployment?
#
# This graph helps answer that.
# --------------------------------------------------

# --------------------------------------------------
# STEP 6: LABOUR PARTICIPATION ANALYSIS
# --------------------------------------------------

print("\nCreating Labour Participation Graph...")

plt.figure(figsize=(10,6))

sns.histplot(
    df['Estimated Labour Participation Rate (%)'],
    kde=True
)

plt.title(
    "Labour Participation Rate Distribution"
)

plt.xlabel(
    "Labour Participation Rate (%)"
)

plt.savefig(
    "labour_participation.png"
)

plt.show()

# --------------------------------------------------
# LEARNING:
#
# Labour Participation Rate tells us:
#
# How many people are working
# or actively looking for work.
# --------------------------------------------------

# --------------------------------------------------
# STEP 7: CORRELATION HEATMAP
# --------------------------------------------------

print("\nCreating Correlation Heatmap...")

# Select only numerical columns

numeric_data = df.select_dtypes(
    include='number'
)

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title(
    "Correlation Heatmap"
)

plt.savefig(
    "correlation_heatmap.png"
)

plt.show()

# --------------------------------------------------
# LEARNING:
#
# Correlation Values:
#
# +1  = Strong Positive Relation
# 0   = No Relation
# -1  = Strong Negative Relation
# --------------------------------------------------

# --------------------------------------------------
# STEP 8: COVID-19 ANALYSIS
# --------------------------------------------------

print("\nLoading COVID Dataset...")

covid_df = pd.read_csv(
    "Unemployment_Rate_upto_11_2020.csv"
)

covid_df.columns = covid_df.columns.str.strip()

covid_df['Date'] = pd.to_datetime(
    covid_df['Date'],
    dayfirst=True
)

covid_rate = covid_df.groupby(
    'Date'
)['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12,6))

covid_rate.plot()

plt.title(
    "COVID-19 Impact on Unemployment"
)

plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.grid(True)

plt.savefig(
    "covid_unemployment.png"
)

plt.show()

# --------------------------------------------------
# STEP 9: KEY INSIGHTS
# --------------------------------------------------

print("\n===================================")
print("KEY INSIGHTS")
print("===================================")

print("""
1. Unemployment increased significantly
   during the COVID-19 period.

2. Some states consistently experienced
   higher unemployment rates.

3. Labour participation varied across
   different regions.

4. Economic disruptions had a visible
   impact on employment trends.
""")

print("\nProject Completed Successfully!")