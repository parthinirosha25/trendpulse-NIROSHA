# ============================================================================
# Project: TrendPulse - What's Actually Trending Right Now
# File: task4_visualization.py
# Programmer-Name: Nirosha. N - Executed date (09/27/2026)
# Purpose:
"""This script visualises the analysed TrendPulse data
using Matplotlib."""
# ============================================================================

# Import Pandas for loading and preparing the data.
import pandas as pd
# Import Matplotlib for creating charts.
import matplotlib.pyplot as plt
# Import os for creating the output folder.
import os

# ============================================================
# Step-1: Load analysed data
# ============================================================
# Load the analysed CSV file created in Task 3.
df = pd.read_csv("data/trends_analysed.csv")

# Print the number of stories loaded.
print("Loaded row count:", len(df))

# ============================================================
# Step-2: Create output folder
# ============================================================

# Create the outputs folder if it does not already exist.
os.makedirs("outputs", exist_ok=True)

# ============================================================
# Step-3: Chart 1 - Top 10 stories by score
# ============================================================

# Sort stories by score from highest to lowest.
top_10_stories = df.sort_values("score", ascending=False).head(10)

# Create a horizontal bar chart.
plt.barh(top_10_stories["title"], top_10_stories["score"])

# Add a title to the chart.
plt.title("Top 10 Stories by Score")

# Add a label to the x-axis.
plt.xlabel("Score")

# Add a label to the y-axis.
plt.ylabel("Story")

# Reverse the y-axis so the highest score appears at the top.
plt.gca().invert_yaxis()

# Adjust the layout so story titles fit properly.
plt.tight_layout()

# Save the chart as a PNG file.
plt.savefig("outputs/chart1_top_stories.png")

# Display the chart.
plt.show()

# Close the current figure.
plt.close()

# ============================================================
# Step-4: Chart 2 - Number of stories by category
# ============================================================

# Count the number of stories in each category.
category_counts = df["category"].value_counts()

# Create a bar chart using the category counts.
plt.bar(category_counts.index, category_counts.values)

# Add a title to the chart.
plt.title("Number of Stories by Category")

# Add a label to the x-axis.
plt.xlabel("Category")

# Add a label to the y-axis.
plt.ylabel("Number of Stories")

# Adjust the layout for better spacing.
plt.tight_layout()

# Save the chart as a PNG file.
plt.savefig("outputs/chart2_categories.png")

# Display the chart.
plt.show()

# Close the current figure.
plt.close()

# ============================================================
# Step-5: Chart 3 - Score versus number of comments
# ============================================================

# Separate popular stories from non-popular stories.
popular_stories = df[df["is_popular"] == True]
non_popular_stories = df[df["is_popular"] == False]

# Create a scatter plot for popular stories.
plt.scatter(
    popular_stories["score"],
    popular_stories["num_comments"],
    label="Popular"
)

# Create a scatter plot for non-popular stories.
plt.scatter(
    non_popular_stories["score"],
    non_popular_stories["num_comments"],
    label="Non-Popular"
)

# Add a title to the chart.
plt.title("Score vs Number of Comments")

# Add a label to the x-axis.
plt.xlabel("Score")

# Add a label to the y-axis.
plt.ylabel("Number of Comments")

# Display the legend.
plt.legend()

# Adjust the layout for better spacing.
plt.tight_layout()

# Save the chart as a PNG file.
plt.savefig("outputs/chart3_scatter.png")

# Display the chart.
plt.show()

# Close the current figure.
plt.close()

