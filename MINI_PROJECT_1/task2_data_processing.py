# ============================================================================
# Project: TrendPulse - What's Actually Trending Right Now
# File: task2_data_processing.py
# Programmer-Name: Nirosha. N - Executed date (09/26/2026)
# Purpose:
"""This script loads the JSON data collected in Task 1,
cleans the data using Pandas, and saves the cleaned data as a CSV file."""

# Data Processing Flow:
# Load JSON --> Remove duplicates --> Handle missing values
# --> Fix data types --> Remove low-score stories
# --> Clean whitespace --> Save as CSV
# ============================================================================

# Import Pandas for data processing.
import pandas as pd

# ============================================================
# Step-1: Load JSON data
# ============================================================

# Load the JSON file created by Task 1 into a Pandas DataFrame.
df = pd.read_json("Data/trends_20260926.json")

# Print the number of stories loaded from the JSON file.
print("Loaded row count:", len(df))

# ============================================================
# Step-2: Remove duplicate stories
# ============================================================

# Remove duplicate stories based on post_id.
df = df.drop_duplicates(subset="post_id")

# ============================================================
# Step-3: Remove rows with missing values
# ============================================================

# Remove rows where post_id, title, or score is missing.
df = df.dropna(subset=["post_id", "title", "score"])

# ============================================================
# Step-4: Ensure correct data types
# ============================================================

# Convert score and num_comments columns to integer data types.
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# ============================================================
# Step-5: Remove low-quality records
# ============================================================

# Remove stories with a score below 5.
df = df[df["score"] >= 5]

# ============================================================
# Step-6: Clean title whitespace
# ============================================================

# Remove extra whitespace from the beginning and end of each title.
df["title"] = df["title"].str.strip()

# ============================================================
# Step-7: Save cleaned data as CSV
# ============================================================

# Save the cleaned data as a CSV file.
# index=False prevents Pandas from adding its own row numbers.
df.to_csv("data/trends_clean.csv", index=False)

# ============================================================
# Step-8: Print final results
# ============================================================

# Print the number of stories remaining after cleaning.
print("Final row count:", len(df))

# Print the number of stories in each category.
print("\nStories per category:")
print(df["category"].value_counts())


