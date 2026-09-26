
Your repository should eventually look like this:

trendpulse-yourname/
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
│
├── data/
│   ├── trends_YYYYMMDD.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
│
└── outputs/
    ├── chart1_top_stories.png
    ├── chart2_categories.png
    └── chart3_scatter.png
    
And the pipeline is:

             HACKER NEWS API
                    ↓
        ┌───────────────────────┐
        │ TASK 1                │
        │ Fetch JSON            │
        └───────────┬───────────┘
                    ↓
           trends_YYYYMMDD.json
                    ↓
        ┌───────────────────────┐
        │ TASK 2                │
        │ Clean with Pandas     │
        └───────────┬───────────┘
                    ↓
            trends_clean.csv
                    ↓
        ┌───────────────────────┐
        │ TASK 3                │
        │ Pandas + NumPy        │
        └───────────┬───────────┘
                    ↓
           trends_analysed.csv
                    ↓
        ┌───────────────────────┐
        │ TASK 4                │
        │ Matplotlib            │
        └───────────┬───────────┘
                    ↓
                 3 PNGs

1. Ask HackerNews for top story IDs (https://hacker-news.firebaseio.com/v0/topstories.json?utm_source=chatgpt.com)
                ↓
2. Take first 500 IDs
                ↓
3. Get details for each story
                ↓
4. Look at story title
                ↓
5. Check keywords
                ↓
6. Assign one of 5 categories
                ↓
7. Collect maximum 25 per category
                ↓
8. Extract 7 required fields
                ↓
9. Save everything as JSON
                ↓
10. Print total collected
                 
    
Step -1: 1. Ask HackerNews for top story IDs

Your Python program
       │
       │ GET request
       ↓
Hacker News API
       │
       │ JSON response
       ↓
[49855315, 49854693, 49855018, ...]
       │
       ↓
Story IDs




