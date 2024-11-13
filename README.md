Influencer Collaboration Recommendation
Overview:

Find the Best Collaboration Match: Based on influencer metrics like Followers, Engagement Rate, and Likes Avg., the script computes the best collaboration match using cosine similarity.
Compare Influencers: The script also allows users to compare two influencers by their Followers and Likes Avg. through a bar graph.

Features
1. Best Collaboration Match
Given the Followers, Engagement Rate, and Likes Avg., it computes a similarity score between influencers using cosine similarity.
Based on the similarity score,it recommends a collaboration type:
Joint Content: Similarity score >= 0.95
Cross-promotion: Similarity score >= 0.85
Shout-out: Similarity score < 0.85
2. Influencer Comparison
Users can select two influencers to compare their Followers and Likes Avg. values.
It will display a bar graph comparing the two influencers on these metrics.
Technologies Used:
Python: Core language used for data processing.
Pandas: For handling and processing the CSV data.
Scikit-learn: For calculating cosine similarity between influencer metrics.
Plotly: To create an interactive bar chart for comparing influencers.
