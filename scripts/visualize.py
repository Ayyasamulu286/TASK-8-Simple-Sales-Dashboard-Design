"""
Superstore Sales - Visualizations for all 8 Tasks
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_excel("data/Superstore_Sales_600_Records.xlsx")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month']      = df['Order Date'].dt.month
df['Month_Name'] = df['Order Date'].dt.strftime('%B')
df['Quarter']    = df['Order Date'].dt.quarter
df['Profit_Margin_%'] = (df['Profit'] / df['Sales'] * 100).round(2)

COLORS = ['#2196F3','#4CAF50','#FF9800','#E91E63','#9C27B0']
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white'})

# ── Fig 1: Task 1 – Region Sales & Profit ────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
t1 = df.groupby('Region')[['Sales','Profit']].sum().reset_index()
axes[0].bar(t1['Region'], t1['Sales'], color=COLORS[:4])
axes[0].set_title('Task 1: Total Sales by Region', fontweight='bold')
axes[0].set_ylabel('Sales ($)')
for i, v in enumerate(t1['Sales']): axes[0].text(i, v+500, f'${v:,.0f}', ha='center', fontsize=9)
axes[1].bar(t1['Region'], t1['Profit'], color=COLORS[:4])
axes[1].set_title('Task 1: Total Profit by Region', fontweight='bold')
axes[1].set_ylabel('Profit ($)')
for i, v in enumerate(t1['Profit']): axes[1].text(i, v+200, f'${v:,.0f}', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('outputs/task1_region.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Fig 2: Task 2 – Category Performance ─────────────────────────────────────
t2 = df.groupby('Category')[['Sales','Profit']].sum().reset_index()
fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(t2))
bars1 = ax.bar(x - 0.2, t2['Sales'], 0.4, label='Sales', color='#2196F3')
bars2 = ax.bar(x + 0.2, t2['Profit'], 0.4, label='Profit', color='#4CAF50')
ax.set_xticks(x); ax.set_xticklabels(t2['Category'])
ax.set_title('Task 2: Category-wise Sales vs Profit', fontweight='bold')
ax.set_ylabel('Amount ($)'); ax.legend()
plt.tight_layout()
plt.savefig('outputs/task2_category.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Fig 3: Task 3 – Monthly Trend ────────────────────────────────────────────
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
t3 = df.groupby(['Month','Month_Name'])['Sales'].sum().reset_index().sort_values('Month')
fig, ax = plt.subplots(figsize=(13, 5))
ax.plot(range(len(t3)), t3['Sales'], marker='o', color='#2196F3', linewidth=2)
ax.fill_between(range(len(t3)), t3['Sales'], alpha=0.15, color='#2196F3')
ax.set_xticks(range(len(t3))); ax.set_xticklabels([m[:3] for m in t3['Month_Name']], rotation=0)
ax.set_title('Task 3: Monthly Sales Trend', fontweight='bold')
ax.set_ylabel('Sales ($)')
for i, v in enumerate(t3['Sales']): ax.annotate(f'${v:,.0f}', (i, v), textcoords="offset points", xytext=(0,8), ha='center', fontsize=8)
plt.tight_layout()
plt.savefig('outputs/task3_monthly.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Fig 4: Task 4 – Top 10 Orders ────────────────────────────────────────────
t4 = df.nlargest(10, 'Profit').reset_index(drop=True)
t4['Label'] = t4['Category'] + '\n' + t4['Region']
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(range(len(t4)), t4['Profit'], color=COLORS[0])
ax.set_yticks(range(len(t4))); ax.set_yticklabels(t4['Label'], fontsize=9)
ax.invert_yaxis()
ax.set_title('Task 4: Top 10 Most Profitable Orders', fontweight='bold')
ax.set_xlabel('Profit ($)')
for i, v in enumerate(t4['Profit']): ax.text(v+2, i, f'${v:.0f}', va='center', fontsize=9)
plt.tight_layout()
plt.savefig('outputs/task4_top10.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Fig 5: Task 5 – Margin Distribution ──────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df['Profit_Margin_%'], bins=30, color='#2196F3', edgecolor='white', alpha=0.8)
ax.axvline(10, color='red', linestyle='--', linewidth=2, label='10% threshold')
ax.set_title('Task 5: Profit Margin Distribution', fontweight='bold')
ax.set_xlabel('Profit Margin (%)'); ax.set_ylabel('Count'); ax.legend()
low = (df['Profit_Margin_%'] < 10).sum()
ax.text(0.02, 0.95, f'Low-margin orders: {low}', transform=ax.transAxes, color='red', fontsize=10)
plt.tight_layout()
plt.savefig('outputs/task5_margin_dist.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Fig 6: Task 6 – Quarterly ─────────────────────────────────────────────────
t6 = df.groupby('Quarter')[['Sales','Profit']].sum().reset_index()
t6['Quarter'] = 'Q' + t6['Quarter'].astype(str)
fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(t6))
ax.bar(x - 0.2, t6['Sales'], 0.4, label='Sales', color='#2196F3')
ax.bar(x + 0.2, t6['Profit'], 0.4, label='Profit', color='#4CAF50')
ax.set_xticks(x); ax.set_xticklabels(t6['Quarter'])
ax.set_title('Task 6: Quarterly Sales vs Profit', fontweight='bold')
ax.set_ylabel('Amount ($)'); ax.legend()
plt.tight_layout()
plt.savefig('outputs/task6_quarterly.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Fig 7: Task 7 – Heatmap ───────────────────────────────────────────────────
t7 = df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum')
fig, ax = plt.subplots(figsize=(9, 5))
im = ax.imshow(t7.values, cmap='Blues', aspect='auto')
ax.set_xticks(range(len(t7.columns))); ax.set_xticklabels(t7.columns)
ax.set_yticks(range(len(t7.index))); ax.set_yticklabels(t7.index)
for i in range(len(t7.index)):
    for j in range(len(t7.columns)):
        ax.text(j, i, f'${t7.values[i,j]:,.0f}', ha='center', va='center', fontsize=10, fontweight='bold')
plt.colorbar(im, ax=ax, label='Sales ($)')
ax.set_title('Task 7: Region × Category Sales Heatmap', fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/task7_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()

# ── Fig 8: Task 8 – KPI Dashboard ─────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Task 8: KPI Summary Dashboard', fontweight='bold', fontsize=14)

# Pie: sales by region
t1r = df.groupby('Region')['Sales'].sum()
axes[0,0].pie(t1r.values, labels=t1r.index, autopct='%1.1f%%', colors=COLORS[:4], startangle=90)
axes[0,0].set_title('Sales Share by Region')

# Pie: sales by category
t2c = df.groupby('Category')['Sales'].sum()
axes[0,1].pie(t2c.values, labels=t2c.index, autopct='%1.1f%%', colors=['#2196F3','#4CAF50','#FF9800'], startangle=90)
axes[0,1].set_title('Sales Share by Category')

# Bar: quarterly profit
axes[1,0].bar(t6['Quarter'], t6['Profit'], color=['#2196F3','#4CAF50','#FF9800','#E91E63'])
axes[1,0].set_title('Profit by Quarter'); axes[1,0].set_ylabel('Profit ($)')

# Bar: monthly profit top months
monthly_profit = df.groupby('Month_Name')['Profit'].sum()
top_months = monthly_profit.nlargest(6)
axes[1,1].bar(range(len(top_months)), top_months.values, color='#4CAF50')
axes[1,1].set_xticks(range(len(top_months))); axes[1,1].set_xticklabels(top_months.index, rotation=30, fontsize=9)
axes[1,1].set_title('Top 6 Months by Profit')

plt.tight_layout()
plt.savefig('outputs/task8_dashboard.png', dpi=150, bbox_inches='tight')
plt.close()

print("✅ All 8 visualizations saved in outputs/")
