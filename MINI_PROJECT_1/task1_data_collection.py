# ============================================================================
# Project: TrendPulse - What's Actually Trending Right Now
# File: task1_data_collection.py
# Programmer-Name: Nirosha. N - Executed date (09/27/2026)
# Purpose:
"""This script collects the first 500 top story IDs from the
Hacker News API. These story IDs will be used to fetch individual
story details such as title, score, number of comments, and author."""

# Data Collection Flow:
# Hacker News API --> Get top story IDs --> Select first 500 IDs
# --> Fetch individual story details --> Check title keywords
# --> Assign category --> Store stories --> Save as JSON
# ============================================================================

# Import the requests library to send HTTP requests to fetch Hacker News API.
import requests
from datetime import datetime
import json
import os
import time

# Define the Hacker News API endpoint that provides the IDs of the current top stories.
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Define a User-Agent header to identify our application when sending requests.
headers = {
    "User-Agent": "TrendPulse/1.0"
}

# ============================================================
# Step-1: Get the top story IDs
# ============================================================

# Send a GET request to the Hacker News top stories endpoint.
response = requests.get(top_stories_url, headers=headers)

# Print the HTTP status code to check whether the API request was successful.
print("Status code: ", response.status_code)

# Convert the API response from JSON format into a Python list
# and select only the first 500 story IDs.
top_story_ids = response.json()[:500]

# Print the number of story IDs collected.
print("No.Of Stories: ", len(top_story_ids))

# ============================================================
# Step-2: Define categories and their keywords
# ============================================================

"""The keywords below are taken directly from the assignment.
They will be matched against story titles.
Matching will be case-insensitive."""

category_keywords = {

    "technology": [
        "AI", "software", "tech", "code", "computer",
        "data", "cloud", "API", "GPU", "LLM"
    ],

    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],

    "sports": [
        "NFL", "NBA", "FIFA", "sport", "game",
        "team", "player", "league", "championship"
    ],

    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "NASA", "genome"
    ],

    "entertainment": [
        "movie", "film", "music", "Netflix", "game",
        "book", "show", "award", "streaming"
    ]
}


# ============================================================
# Step-3: Create storage for collected stories
# ============================================================

# Create an empty dictionary to store stories for each category.
# Each category can contain a maximum of 25 stories.

category_stories = {
    "technology": [],
    "worldnews": [],
    "sports": [],
    "science": [],
    "entertainment": []
}


# ============================================================
# Step-4: Fetch details for all 500 story IDs
# ============================================================

# Loop through each category and its keywords.
for category, keywords in category_keywords.items():

    # Loop through the 500 top story IDs.
    for story_id in top_story_ids:

        # Stop collecting when this category has 25 stories.
        if len(category_stories[category]) >= 25:
            break

        try:

            # Create the API URL for the current story ID.
            story_url = (
                f"https://hacker-news.firebaseio.com/v0/item/"
                f"{story_id}.json"
            )

            # Send a GET request to retrieve the story details.
            story_response = requests.get(
                story_url,
                headers=headers
            )

            # Convert the response into a Python dictionary.
            story = story_response.json()

            # Get the story title.
            title = story.get("title", "")

            # Convert the title to lowercase for
            # case-insensitive keyword matching.
            title_lower = title.lower()

            # Check whether any keyword exists in the title.
            if any(
                keyword.lower() in title_lower
                for keyword in keywords
            ):

                # Create the dictionary containing
                # the 7 required fields.
                collected_story = {
                    "post_id": story.get("id"),
                    "title": story.get("title", ""),
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", ""),
                    "collected_at": datetime.now().isoformat()
                }

                # Add the story to the current category.
                category_stories[category].append(collected_story)

                # Print the category and title.
                print(f"Category: {category}")
                print(f"Title: {title}")

        except Exception as error:

            # Print the error and continue with
            # the next story.
            print(
                f"Failed to fetch story {story_id}: {error}"
            )
            continue

    # Wait 2 seconds before processing the next category.
    time.sleep(2)

# ============================================================
# Step-5: Save collected stories as JSON
# ============================================================

# Create the data folder if it does not already exist.
os.makedirs("data", exist_ok=True)

# Get today's date in YYYYMMDD format.
today = datetime.now().strftime("%Y%m%d")

# Create the output JSON file path.
output_file = f"data/trends_{today}.json"

# Create an empty list to store all collected stories.
all_stories = []

# Add stories from each category into the main list.
for category in category_stories:
    all_stories.extend(category_stories[category])

# Open the JSON file in write mode.
with open(output_file, "w", encoding="utf-8") as file:

    # Save all collected stories as formatted JSON.
    json.dump(
        all_stories,
        file,
        indent=4,
        ensure_ascii=False
    )

# Print the total number of stories collected.
print(f"Collected {len(all_stories)} stories.")

# Print the location of the saved JSON file.
print(f"Saved to {output_file}")