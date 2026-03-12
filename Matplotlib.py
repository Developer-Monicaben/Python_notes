import matplotlib.pyplot as plt

# Sample data
regions = ['North', 'South', 'East', 'West']
sales = [25000, 18000, 22000, 27000]

products = ['Product A', 'Product B', 'Product C', 'Product D']
quantities = [100, 150, 90, 120]

# 1. Bar Chart - Sales by Region
plt.figure(figsize=(6, 4))
plt.bar(regions, sales, color='skyblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 2. Pie Chart - Product Distribution
plt.figure(figsize=(5, 5))
plt.pie(quantities, labels=products, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Product Quantity Distribution')
plt.tight_layout()
plt.show()

# 3. Line Chart - Sales Trend
plt.figure(figsize=(6, 4))
plt.plot(regions, sales, marker='o', linestyle='-', color='green')
plt.title('Sales Trend by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Horizontal Bar Chart - Product Quantities
plt.figure(figsize=(6, 4))
plt.barh(products, quantities, color='orange')
plt.title('Quantity Sold by Product')
plt.xlabel('Quantity')
plt.tight_layout()
plt.show()

# 5. Scatter Plot - Sales vs Quantity
plt.figure(figsize=(6, 4))
plt.scatter(sales, quantities[:4], color='purple', marker='*', s=100)
plt.title('Sales vs Quantity')
plt.xlabel('Sales')
plt.ylabel('Quantity')
plt.tight_layout()
plt.show()
