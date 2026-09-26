# ============================================================================
# Project: TrendPulse - What's Actually Trending Right Now
# File: task3_data_analysis.py
# Programmer-Name: Nirosha. N - Executed date (09/27/2026)
# Purpose:
"""This script analyses the cleaned TrendPulse data using
Pandas and NumPy to identify trending patterns."""
# ============================================================================

# Import Pandas for data analysis.
import pandas as pd
# Import NumPy for numerical calculations.
import numpy as np

# ============================================================
# Step-1: Load cleaned CSV data
# ============================================================

# Load the cleaned CSV file into a Pandas DataFrame.
df = pd.read_csv("data/trends_clean.csv")

# Print the number of rows loaded.
print("Loaded row count:", len(df))

# Display the first five rows.
print("\nFirst five rows:")
print(df.head())

# ============================================================
# Step-2: Find top stories by score
# ============================================================

# Sort the stories based on score from highest to lowest.
top_stories = df.sort_values("score", ascending=False)

# Select the top 10 stories.
top_10_stories = top_stories.head(10)

# Display the top 10 stories.
print("\nTop 10 stories by score:")
print(top_10_stories[["title", "category", "score"]])

# ============================================================
# Step-3: Calculate average score by category
# ============================================================

# Calculate the average score for each category.
average_score = df.groupby("category")["score"].mean()

# Display the average score for each category.
print("\nAverage score by category:")
print(average_score)

# ============================================================
# Step-4: Calculate average comments by category
# ============================================================

# Calculate the average number of comments for each category.
average_comments = df.groupby("category")["num_comments"].mean()

# Display the average comments for each category.
print("\nAverage comments by category:")
print(average_comments)

# ============================================================
# Step-5: Find the most-commented stories
# ============================================================

# Sort stories based on the number of comments from highest to lowest.
most_commented = df.sort_values("num_comments", ascending=False)

# Select the top 10 most-commented stories.
top_10_commented = most_commented.head(10)

# Display the top 10 most-commented stories.
print("\nTop 10 most-commented stories:")
print(top_10_commented[["title", "category", "num_comments"]])

# ============================================================
# Step-6: Calculate score statistics using NumPy
# ============================================================

# Calculate the average score using NumPy.
average_score_all = np.mean(df["score"])

# Calculate the median score using NumPy.
median_score = np.median(df["score"])

# Find the highest score using NumPy.
highest_score = np.max(df["score"])

# Find the lowest score using NumPy.
lowest_score = np.min(df["score"])


# Display the score statistics.
print("\nOverall score statistics:")
print("Average score:", average_score_all)
print("Median score:", median_score)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

# ============================================================
# Step-7: Inspect DataFrame shape
# ============================================================

# Print the number of rows and columns in the DataFrame.
print("\nDataFrame shape:")
print(df.shape)

# ============================================================
# Step-8: Calculate overall averages
# ============================================================

# Calculate the overall average score.
overall_average_score = df["score"].mean()

# Calculate the overall average number of comments.
overall_average_comments = df["num_comments"].mean()

# Display the overall averages.
print("\nOverall averages:")
print("Average score:", overall_average_score)
print("Average comments:", overall_average_comments)


# ============================================================
# Step-9: Calculate standard deviation using NumPy
# ============================================================

# Calculate the standard deviation of the story scores.
score_std = np.std(df["score"])

# Display the standard deviation.
print("\nScore standard deviation:")
print(score_std)

# ============================================================
# Step-10: Find the category with the most stories
# ============================================================

# Count the number of stories in each category.
category_counts = df["category"].value_counts()

# Find the category with the highest number of stories.
most_stories_category = category_counts.idxmax()

# Display the category with the most stories.
print("\nCategory with the most stories:")
print(most_stories_category)

# Display the story count for each category.
print("\nStory count by category:")
print(category_counts)

# ============================================================
# Step-11: Find the story with the most comments
# ============================================================

# Find the row containing the highest number of comments.
most_commented_story = df.loc[df["num_comments"].idxmax()]

# Display the most-commented story.
print("\nStory with the most comments:")
print("Title:", most_commented_story["title"])
print("Category:", most_commented_story["category"])
print("Comments:", most_commented_story["num_comments"])

# ============================================================
# Step-12: Create engagement column
# ============================================================

# Calculate the engagement value for each story.
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Display the engagement values.
print("\nEngagement column:")
print(df[["title", "score", "num_comments", "engagement"]].head())

# ============================================================
# Step-13: Create is_popular column
# ============================================================

# Mark a story as popular if its score is greater than the average score.
df["is_popular"] = df["score"] > overall_average_score

# Display the is_popular values.
print("\nPopular story status:")
print(df[["title", "score", "is_popular"]].head())

# ============================================================
# Step-14: Save analysed data
# ============================================================

# Save the analysed DataFrame as a CSV file.
# index=False prevents Pandas from adding row numbers.
df.to_csv("data/trends_analysed.csv", index=False)

# Confirm that the analysed data has been saved.
print("\nAnalysed data saved to: data/trends_analysed.csv")


