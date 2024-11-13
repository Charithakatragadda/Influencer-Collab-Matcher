Influencer Collab matcher 
Overview
This Streamlit-based web application allows users to:

Find the Best Collaboration Match: Based on metrics such as Followers, Engagement Rate, and Likes Avg., the app recommends the best collaboration match for a selected influencer.
Compare Influencers: Users can compare two influencers side by side based on Followers and Likes Avg. metrics through a bar graph.
The app uses machine learning (cosine similarity) to find the best match for influencers and visualize the comparisons between them.

Features
1. Best Collaboration Match
Given an influencer's Followers, Engagement Rate, and Likes Avg., the app computes the best collaboration match based on similarity scores.
The app recommends a collaboration type based on the similarity score:
Joint Content: Similarity score >= 0.95
Cross-promotion: Similarity score >= 0.85
Shout-out: Similarity score < 0.85
2. Influencer Comparison
Users can compare two influencers' Followers and Likes Avg. values visually using a bar chart.
This feature allows users to see a side-by-side comparison of the key metrics for two influencers of their choice.
Technologies Used
Python: The core language for the app.
Streamlit: Used for creating the interactive web interface.
Plotly: For generating dynamic and interactive bar charts.
Pandas: For data manipulation and handling CSV file operations.
Scikit-learn: For calculating cosine similarity between influencer metrics.
