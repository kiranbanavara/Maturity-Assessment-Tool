"""
Visualization components for the maturity assessment tool.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from categories import CATEGORIES, MATURITY_LEVELS

def display_category_radar_chart(scores):
    """
    Display a radar chart of category scores.
    
    Args:
        scores (dict): Dictionary of category scores.
    """
    # Prepare data for radar chart
    categories = []
    values = []
    
    for category_id, category in CATEGORIES.items():
        if category_id in scores and scores[category_id] is not None:
            categories.append(category["name"])
            values.append(scores[category_id])
    
    if not categories:
        st.info("No scores available to display.")
        return
    
    # Create radar chart using Plotly
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Current Assessment'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )
        ),
        showlegend=True,
        title="Category Maturity Scores"
    )
    
    st.plotly_chart(fig, use_container_width=True)

def display_score_gauges(scores):
    """
    Display gauge charts for overall and category scores.
    
    Args:
        scores (dict): Dictionary of category scores and overall score.
    """
    # Create a row for the overall score gauge
    if "overall" in scores and scores["overall"] is not None:
        st.subheader("Overall Maturity Score")
        overall_score = scores["overall"]
        
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=overall_score,
            title={"text": "Overall Maturity"},
            gauge={
                "axis": {"range": [0, 5], "tickwidth": 1, "tickcolor": "darkblue"},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [0, 1], "color": "red"},
                    {"range": [1, 2], "color": "orange"},
                    {"range": [2, 3], "color": "yellow"},
                    {"range": [3, 4], "color": "lightgreen"},
                    {"range": [4, 5], "color": "green"}
                ]
            }
        ))
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Display interpretation
        maturity_level = int(overall_score)
        st.info(f"**Maturity Level: {maturity_level}**\n\n{MATURITY_LEVELS[maturity_level]}")
    
    # Create gauges for each category
    st.subheader("Category Scores")
    
    # Create columns for category gauges
    cols = st.columns(3)
    
    i = 0
    for category_id, category in CATEGORIES.items():
        if category_id in scores and scores[category_id] is not None:
            with cols[i % 3]:
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=scores[category_id],
                    title={"text": category["name"]},
                    gauge={
                        "axis": {"range": [0, 5], "tickwidth": 1, "tickcolor": "darkblue"},
                        "bar": {"color": "darkblue"},
                        "steps": [
                            {"range": [0, 1], "color": "red"},
                            {"range": [1, 2], "color": "orange"},
                            {"range": [2, 3], "color": "yellow"},
                            {"range": [3, 4], "color": "lightgreen"},
                            {"range": [4, 5], "color": "green"}
                        ]
                    }
                ))
                
                st.plotly_chart(fig, use_container_width=True)
                i += 1

def display_question_responses_chart(responses):
    """
    Display a bar chart of question responses.
    
    Args:
        responses (dict): Dictionary of question IDs and their responses.
    """
    st.subheader("Response Distribution")
    
    # Prepare data for the chart
    data = []
    
    for category_id, category in CATEGORIES.items():
        for question in category["questions"]:
            question_id = question["id"]
            
            if question_id in responses and responses[question_id] != "NA":
                # Map binary responses to their numeric value
                if question["type"] == "binary":
                    value = 5 if responses[question_id] == "Yes" else 0
                else:
                    value = int(responses[question_id])
                
                data.append({
                    "Category": category["name"],
                    "Question": question["text"],
                    "Score": value
                })
    
    if not data:
        st.info("No responses available to display.")
        return
    
    # Create DataFrame and chart
    df = pd.DataFrame(data)
    
    fig = px.bar(
        df,
        x="Score",
        y="Question",
        color="Category",
        orientation="h",
        title="Question Responses by Category",
        labels={"Score": "Response Value (0-5)"},
        range_x=[0, 5]
    )
    
    st.plotly_chart(fig, use_container_width=True)

def display_strength_weakness_analysis(scores, responses):
    """
    Display an analysis of strengths and weaknesses based on responses.
    
    Args:
        scores (dict): Dictionary of category scores.
        responses (dict): Dictionary of question IDs and their responses.
    """
    st.subheader("Strengths & Improvement Opportunities")
    
    # Prepare data for analysis
    strengths = []
    weaknesses = []
    
    for category_id, category in CATEGORIES.items():
        for question in category["questions"]:
            question_id = question["id"]
            
            if question_id in responses and responses[question_id] != "NA":
                # Map binary responses to their numeric value
                if question["type"] == "binary":
                    value = 5 if responses[question_id] == "Yes" else 0
                else:
                    value = int(responses[question_id])
                
                if value >= 4:
                    strengths.append({
                        "category": category["name"],
                        "question": question["text"],
                        "score": value
                    })
                elif value <= 2:
                    weaknesses.append({
                        "category": category["name"],
                        "question": question["text"],
                        "score": value
                    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Strengths")
        if strengths:
            strengths.sort(key=lambda x: x["score"], reverse=True)
            for item in strengths:
                st.success(f"**{item['category']}**: {item['question']} (Score: {item['score']})")
        else:
            st.info("No specific strengths identified.")
    
    with col2:
        st.markdown("#### Improvement Opportunities")
        if weaknesses:
            weaknesses.sort(key=lambda x: x["score"])
            for item in weaknesses:
                st.warning(f"**{item['category']}**: {item['question']} (Score: {item['score']})")
        else:
            st.info("No specific improvement opportunities identified.")

def display_maturity_heatmap(scores):
    """
    Display a heatmap of maturity scores by category.
    
    Args:
        scores (dict): Dictionary of category scores.
    """
    st.subheader("Maturity Heatmap")
    
    # Prepare data for heatmap
    categories = []
    values = []
    
    for category_id, category in CATEGORIES.items():
        if category_id in scores and scores[category_id] is not None:
            categories.append(category["name"])
            values.append(scores[category_id])
    
    if not categories:
        st.info("No scores available to display.")
        return
    
    # Create a single row DataFrame for the heatmap
    df = pd.DataFrame([values], columns=categories)
    
    # Create heatmap
    fig = px.imshow(
        df,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale=[
            (0, "red"),
            (0.2, "orange"),
            (0.4, "yellow"),
            (0.6, "lightgreen"),
            (0.8, "green"),
            (1, "darkgreen")
        ],
        range_color=[0, 5],
        title="Maturity Level by Category"
    )
    
    fig.update_layout(
        coloraxis_colorbar=dict(
            title="Score",
            tickvals=[0, 1, 2, 3, 4, 5],
            ticktext=["0", "1", "2", "3", "4", "5"]
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
