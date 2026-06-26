"""
Superstore Sales Analysis - All 8 Tasks
Dataset: 600 records with columns: Order Date, Region, Category, Sales, Profit
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json
import os

# ─── Load Data ───────────────────────────────────────────────────────────────
df = pd.read_excel("data/Superstore_Sales_600_Records.xlsx")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month']      = df['Order Date'].dt.month
df['Month_Name'] = df['Order Date'].dt.strftime('%B')
df['Quarter']    = df['Order Date'].dt.quarter
df['Year']       = df['Order Date'].dt.year

os.makedirs("outputs", exist_ok=True)

print("=" * 60)
print("  SUPERSTORE SALES ANALYSIS — 8 TASKS")
print("=" * 60)

# ─── TASK 1: Total Sales and Profit by Region ────────────────────────────────
print("\n📌 TASK 1: Total Sales and Profit by Region")
t1 = df.groupby('Region')[['Sales','Profit']].sum().round(2).reset_index()
t1['Profit_Margin_%'] = (t1['Profit'] / t1['Sales'] * 100).round(2)
print(t1.to_string(index=False))
t1.to_csv("outputs/task1_region_analysis.csv", index=False)

# ─── TASK 2: Category-wise Performance ───────────────────────────────────────
print("\n📌 TASK 2: Category-wise Performance")
t2 = df.groupby('Category').agg(
    Total_Sales=('Sales','sum'),
    Avg_Sales=('Sales','mean'),
    Order_Count=('Sales','count'),
    Total_Profit=('Profit','sum'),
    Avg_Profit=('Profit','mean')
).round(2).reset_index()
print(t2.to_string(index=False))
t2.to_csv("outputs/task2_category_analysis.csv", index=False)

# ─── TASK 3: Monthly Sales Trend ─────────────────────────────────────────────
print("\n📌 TASK 3: Monthly Sales Trend")
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
t3 = df.groupby(['Month','Month_Name'])['Sales'].sum().round(2).reset_index()
t3 = t3.sort_values('Month')
print(t3[['Month_Name','Sales']].to_string(index=False))
t3.to_csv("outputs/task3_monthly_trend.csv", index=False)

# ─── TASK 4: Top 10 Most Profitable Orders ───────────────────────────────────
print("\n📌 TASK 4: Top 10 Most Profitable Orders")
t4 = df.nlargest(10, 'Profit')[['Order Date','Region','Category','Sales','Profit']].reset_index(drop=True)
t4['Profit_Margin_%'] = (t4['Profit'] / t4['Sales'] * 100).round(2)
print(t4.to_string(index=False))
t4.to_csv("outputs/task4_top10_orders.csv", index=False)

# ─── TASK 5: Loss-making / Below Average Profit Orders ───────────────────────
print("\n📌 TASK 5: Low-Profit Orders (below 10% margin)")
df['Profit_Margin_%'] = (df['Profit'] / df['Sales'] * 100).round(2)
t5 = df[df['Profit_Margin_%'] < 10][['Order Date','Region','Category','Sales','Profit','Profit_Margin_%']].reset_index(drop=True)
print(f"  Total low-margin orders: {len(t5)}")
print(t5.head(10).to_string(index=False))
t5.to_csv("outputs/task5_low_margin_orders.csv", index=False)

# ─── TASK 6: Quarter-wise Sales Comparison ───────────────────────────────────
print("\n📌 TASK 6: Quarter-wise Sales Comparison")
t6 = df.groupby('Quarter')[['Sales','Profit']].sum().round(2).reset_index()
t6['Quarter'] = 'Q' + t6['Quarter'].astype(str)
t6['Profit_Margin_%'] = (t6['Profit'] / t6['Sales'] * 100).round(2)
print(t6.to_string(index=False))
t6.to_csv("outputs/task6_quarterly.csv", index=False)

# ─── TASK 7: Region × Category Cross Analysis ────────────────────────────────
print("\n📌 TASK 7: Region × Category Sales Matrix")
t7 = df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum').round(2)
print(t7.to_string())
t7.to_csv("outputs/task7_region_category_matrix.csv")

# ─── TASK 8: Summary KPIs Dashboard ─────────────────────────────────────────
print("\n📌 TASK 8: Summary KPIs Dashboard")
t8 = {
    "Total Records": len(df),
    "Total Sales ($)": round(df['Sales'].sum(), 2),
    "Total Profit ($)": round(df['Profit'].sum(), 2),
    "Overall Profit Margin (%)": round(df['Profit'].sum() / df['Sales'].sum() * 100, 2),
    "Avg Order Value ($)": round(df['Sales'].mean(), 2),
    "Best Region by Profit": df.groupby('Region')['Profit'].sum().idxmax(),
    "Worst Region by Profit": df.groupby('Region')['Profit'].sum().idxmin(),
    "Best Category by Sales": df.groupby('Category')['Sales'].sum().idxmax(),
    "Best Category by Profit": df.groupby('Category')['Profit'].sum().idxmax(),
    "Best Quarter by Sales": "Q" + str(df.groupby('Quarter')['Sales'].sum().idxmax()),
    "Most Profitable Month": df.groupby('Month_Name')['Profit'].sum().idxmax(),
    "Low Margin Orders (<10%)": int((df['Profit_Margin_%'] < 10).sum())
}
for k, v in t8.items():
    print(f"  {k:35s}: {v}")
with open("outputs/task8_kpis.json", "w") as f:
    json.dump(t8, f, indent=2)

print("\n✅ All tasks complete. Outputs saved in /outputs/")
