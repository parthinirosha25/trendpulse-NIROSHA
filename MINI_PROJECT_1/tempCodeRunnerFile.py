# using pandas to load the dataframes
import pandas as pd

# Load the JSON file created by Task 1 into a Pandas DataFrame.
df = pd.read_json("data/trends_20260926.json")

# Print the number of stories loaded from the JSON file.
print("Loaded row count:", len(df))
