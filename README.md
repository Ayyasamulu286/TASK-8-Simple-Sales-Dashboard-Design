# 🛒 Superstore Sales Analysis — 8 Tasks

A complete data analysis project on a Superstore Sales dataset (600 records) solving 8 analytical tasks using Python (Pandas + Matplotlib).

## 📁 Project Structure

```
superstore_analysis/
├── data/
│   └── Superstore_Sales_600_Records.xlsx   # Raw dataset
├── scripts/
│   ├── analysis.py                          # All 8 tasks — data analysis
│   └── visualize.py                         # Charts & visualizations
├── outputs/
│   ├── task1_region_analysis.csv
│   ├── task2_category_analysis.csv
│   ├── task3_monthly_trend.csv
│   ├── task4_top10_orders.csv
│   ├── task5_low_margin_orders.csv
│   ├── task6_quarterly.csv
│   ├── task7_region_category_matrix.csv
│   ├── task8_kpis.json
│   └── *.png  (8 chart images)
└── README.md
```

## 📊 Dataset Columns

| Column     | Type   | Description                        |
|------------|--------|------------------------------------|
| Order Date | Date   | Date of the order                  |
| Region     | String | East, West, Central, South         |
| Category   | String | Furniture, Office Supplies, Technology |
| Sales      | Float  | Revenue from the order ($)         |
| Profit     | Float  | Profit from the order ($)          |

## ✅ 8 Tasks Summary

### Task 1 — Total Sales & Profit by Region
Group by Region → sum Sales and Profit → calculate Profit Margin %.

**Result:** Central leads in Sales ($160,259), South leads in Profit Margin (18.41%).

### Task 2 — Category-wise Performance
Group by Category → compute total/average sales, order count, total/average profit.

**Result:** Office Supplies has highest order count (207), Technology has best average profit.

### Task 3 — Monthly Sales Trend
Extract month from Order Date → group and sum Sales → identify peaks.

**Result:** August ($64,453) and June ($63,037) are peak months.

### Task 4 — Top 10 Most Profitable Orders
Sort by Profit descending → take top 10 → show with margin %.

**Result:** Highest profit order: $557.41 (South, Furniture, May 2025).

### Task 5 — Low-Margin Orders (< 10% profit margin)
Compute Profit Margin % per row → filter below 10% threshold.

**Result:** Identified all orders below 10% margin for review.

### Task 6 — Quarter-wise Sales Comparison
Extract Quarter from Order Date → group and compare Q1–Q4.

**Result:** Q3 leads in Sales ($163,979), Q1 leads in Profit Margin (18.56%).

### Task 7 — Region × Category Cross Analysis
Pivot table: Rows = Region, Columns = Category, Values = Sum of Sales.

**Result:** Central-Furniture ($54,822) is the largest segment.

### Task 8 — Summary KPI Dashboard
Aggregate all key metrics: total sales, profit margin, best region, best category, etc.

**Key KPIs:**
- Total Sales: $611,271.62
- Total Profit: $110,300.28
- Overall Profit Margin: 18.04%
- Best Region: Central
- Best Category (Sales): Office Supplies
- Most Profitable Month: August

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/superstore_analysis.git
cd superstore_analysis

# Install dependencies
pip install pandas openpyxl matplotlib numpy

# Run analysis
python scripts/analysis.py

# Run visualizations
python scripts/visualize.py
```

## 🛠 Technologies Used
- Python 3.x
- Pandas — data manipulation
- Matplotlib — charts and visualizations
- OpenPyXL — Excel file reading
- NumPy — numerical operations

## 📈 Output Charts
Each task produces one PNG chart saved in `outputs/`:
- `task1_region.png` — Bar chart: Sales & Profit by Region
- `task2_category.png` — Grouped bar: Category comparison
- `task3_monthly.png` — Line chart: Monthly trend
- `task4_top10.png` — Horizontal bar: Top 10 orders
- `task5_margin_dist.png` — Histogram: Margin distribution
- `task6_quarterly.png` — Grouped bar: Q1–Q4 comparison
- `task7_heatmap.png` — Heatmap: Region × Category matrix
- `task8_dashboard.png` — 4-panel KPI dashboard


Your Name — S Ayyasamulu


