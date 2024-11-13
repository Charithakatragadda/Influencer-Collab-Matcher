import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

st.title("Influencer Collaboration Recommendations")
uploaded_file=r"C:\Users\chari\Downloads\archive\top_200_instagrammers.csv" 
if uploaded_file is not None:
    influencers_df=pd.read_csv(uploaded_file)
    st.write("Uploaded Influencer Data:")
    st.dataframe(influencers_df)
    required_columns={'Username', 'Followers', 'Engagement Rate', 'Likes Avg.'}
    if not required_columns.issubset(influencers_df.columns):
        st.error(f"The uploaded CSV must contain the following columns: {', '.join(required_columns)}")
    else:
        similarities=cosine_similarity(influencers_df[['Followers', 'Engagement Rate', 'Likes Avg.']])
        best_match={}
        for i in range(len(influencers_df)):
            best_similarity=0 
            best_influencer=None
            for j in range(len(influencers_df)):
                if i!=j:
                    if similarities[i, j]>best_similarity: 
                        best_similarity=similarities[i, j]
                        best_influencer=influencers_df['Username'][j]
            best_match[influencers_df['Username'][i]]={
                'Best Match':best_influencer,
                'Similarity Score':best_similarity
            }
        selected_influencer=st.selectbox("Select an Influencer", influencers_df['Username'])
        selected_best_match=best_match[selected_influencer]
        st.subheader(f"Best Match for {selected_influencer}")
        st.write(f"Best Match: {selected_best_match['Best Match']}")
        st.write(f"Similarity Score: {selected_best_match['Similarity Score']:.4f}")
        # Bar chart
        metrics=['Followers', 'Engagement Rate', 'Likes Avg.']
        st.title("Compare any two inflencers")
        influencer_1 = st.selectbox("Select Influencer 1", influencers_df['Username'])
        influencer_2 = st.selectbox("Select Influencer 2", influencers_df['Username'])
        idx1 = influencers_df[influencers_df['Username'] == influencer_1].index[0]
        idx2 = influencers_df[influencers_df['Username'] == influencer_2].index[0]
        influencer1_data=influencers_df.loc[idx1, metrics]
        influencer2_data=influencers_df.loc[idx2, metrics]
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
    