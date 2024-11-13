import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go

st.title("Influencer Collaboration Recommendations")
dataset_path = r"C:\Users\chari\Downloads\archive\top_200_instagrammers.csv" 
try:
    influencers_df = pd.read_csv(dataset_path)
    st.write("Loaded Influencer Data:")
    st.dataframe(influencers_df)
    required_columns = {'Username', 'Followers', 'Engagement Rate', 'Likes Avg.', 'Main video category'}
    if not required_columns.issubset(influencers_df.columns):
        st.error(f"The CSV file must contain the following columns: {', '.join(required_columns)}")
    else:
        scaler = StandardScaler()
        features = ['Followers', 'Engagement Rate', 'Likes Avg.']
        influencers_df[features] = scaler.fit_transform(influencers_df[features])
        similarities = cosine_similarity(influencers_df[features])
        influencer_1 = st.selectbox("Select Influencer 1", influencers_df['Username'])
        influencer_2 = st.selectbox("Select Influencer 2", influencers_df['Username'])
        idx1 = influencers_df[influencers_df['Username'] == influencer_1].index[0]
        idx2 = influencers_df[influencers_df['Username'] == influencer_2].index[0]
        similarity_score = similarities[idx1, idx2]
        st.write(f"Similarity Score between {influencer_1} and {influencer_2}: {similarity_score:.4f}")
        collaboration_type = 'Joint Content' if influencers_df['Engagement Rate'].iloc[idx1] > 0.05 else 'Cross-promotion'
        st.write(f"Recommended Collaboration: {collaboration_type}")
        #Bar chart 
        metrics = ['Followers', 'Engagement Rate', 'Likes Avg.']
        influencer1_data = influencers_df.loc[idx1, metrics]
        influencer2_data = influencers_df.loc[idx2, metrics]
        fig = go.Figure(data=[
            go.Bar(name=influencer_1, x=metrics, y=influencer1_data, marker_color='blue'),
            go.Bar(name=influencer_2, x=metrics, y=influencer2_data, marker_color='red')
        ])
        fig.update_layout(
            title=f"Comparison of Key Metrics: {influencer_1} vs {influencer_2}",
            barmode='group',
            xaxis_title="Metrics",
            yaxis_title="Standardized Values"
        )
        st.plotly_chart(fig)
except FileNotFoundError:
    st.error("The dataset file 'influencers_data.csv' was not found. Please ensure it's in the correct directory.")
