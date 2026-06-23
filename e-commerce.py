# ==========================================
# E-Commerce Sales Performance Analysis
# ==========================================

# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_csv("ecommerce_sales.csv")

# Display Dataset

print("First 5 Records")
print(df.head())

print("\nDataset Info")
print(df.info())

# ------------------------------------------
# Data Cleaning
# ------------------------------------------

# Missing Values

df.fillna(method='ffill', inplace=True)

# Remove Duplicates

df.drop_duplicates(inplace=True)

# Convert Date

df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Month

df['Month'] = df['Order Date'].dt.strftime('%B')

# ------------------------------------------
# Top Selling Products
# ------------------------------------------

product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)

print("\nTop Selling Products")
print(product_sales)

# ------------------------------------------
# Monthly Sales
# ------------------------------------------

monthly_sales = df.groupby('Month')['Sales'].sum()

month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

monthly_sales = monthly_sales.reindex(month_order)

print("\nMonthly Sales")
print(monthly_sales)

# ------------------------------------------
# Bar Chart
# ------------------------------------------

plt.figure(figsize=(10,6))

product_sales.head(10).plot(kind='bar')

plt.title("Top 10 Selling Products")

plt.xlabel("Products")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ------------------------------------------
# Line Chart
# ------------------------------------------

plt.figure(figsize=(10,6))

monthly_sales.plot(marker='o')

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.grid(True)

plt.tight_layout()

plt.show()

# ------------------------------------------
# Final Insights
# ------------------------------------------

print("\nHighest Selling Product:")
print(product_sales.idxmax())

print("\nHighest Revenue:")
print(product_sales.max())

print("\nBest Sales Month:")
print(monthly_sales.idxmax())

print("\nHighest Monthly Revenue:")
print(monthly_sales.max())