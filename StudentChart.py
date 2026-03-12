import pandas as pd
import matplotlib.pyplot as plt

# Read from CSV
df = pd.read_csv("students.csv")

# Count students per standard
standard_counts = df['Standard'].value_counts().sort_index()

# Elegant color palette
colors = plt.cm.Paired(range(len(standard_counts)))  # Professional gradient colors

# Plot
plt.figure(figsize=(10, 6), facecolor='white')
bars = plt.bar(standard_counts.index, standard_counts.values, color=colors, edgecolor='grey', linewidth=1.2)

# Titles and labels
plt.title("📊 Student Count by Standard", fontsize=18, fontweight='bold', color="#333")
plt.xlabel("Standard", fontsize=14)
plt.ylabel("Number of Students", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(range(0, max(standard_counts.values)+1), fontsize=12)

# Grid
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Add clean bar border
for bar in bars:
    bar.set_edgecolor("black")
    bar.set_linewidth(0.8)

# Layout
plt.tight_layout()
plt.show()
