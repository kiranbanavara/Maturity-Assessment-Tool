"""
Module for handling data operations for the maturity assessment tool.
Includes functions for saving, loading, and processing assessment data.
"""

import pandas as pd
import numpy as np
import json
import datetime
import streamlit as st
from categories import CATEGORIES, get_all_question_ids

def initialize_session_state():
    """Initialize the session state variables if they don't exist."""
    if 'current_responses' not in st.session_state:
        st.session_state.current_responses = {}
    
    if 'assessment_history' not in st.session_state:
        st.session_state.assessment_history = []
    
    if 'assessment_date' not in st.session_state:
        st.session_state.assessment_date = datetime.datetime.now().strftime("%Y-%m-%d")

def save_current_responses(responses):
    """Save the current responses to session state."""
    st.session_state.current_responses = responses

def get_current_responses():
    """Get the current responses from session state."""
    return st.session_state.current_responses

def calculate_scores(responses):
    """
    Calculate average scores for each category and overall.
    Excludes 'Not Applicable' responses from the calculations.
    
    Args:
        responses (dict): Dictionary of question IDs and their responses.
    
    Returns:
        dict: A dictionary containing category scores and overall score.
    """
    scores = {}
    all_scores = []
    
    for category_id, category in CATEGORIES.items():
        category_scores = []
        
        for question in category["questions"]:
            question_id = question["id"]
            if question_id in responses and responses[question_id] != "NA":
                # Convert binary responses (Yes/No) to numeric values (5/0)
                if question["type"] == "binary":
                    score = 5 if responses[question_id] == "Yes" else 0
                else:
                    score = int(responses[question_id])
                
                category_scores.append(score)
                all_scores.append(score)
        
        # Calculate average score for the category if there are valid responses
        if category_scores:
            scores[category_id] = sum(category_scores) / len(category_scores)
        else:
            scores[category_id] = None
    
    # Calculate overall average score if there are valid responses
    if all_scores:
        scores["overall"] = sum(all_scores) / len(all_scores)
    else:
        scores["overall"] = None
    
    return scores

def save_assessment(responses, scores, assessment_date):
    """
    Save the current assessment to the history.
    
    Args:
        responses (dict): Dictionary of question IDs and their responses.
        scores (dict): Dictionary of category scores and overall score.
        assessment_date (str): The date of the assessment.
    """
    assessment = {
        "date": assessment_date,
        "responses": responses.copy(),
        "scores": scores
    }
    
    st.session_state.assessment_history.append(assessment)

def get_assessment_history():
    """Get the assessment history from session state."""
    return st.session_state.assessment_history

def clear_current_assessment():
    """Clear the current assessment data."""
    st.session_state.current_responses = {}
    st.session_state.assessment_date = datetime.datetime.now().strftime("%Y-%m-%d")

def export_to_csv(filename="maturity_assessment_history.csv"):
    """
    Export the assessment history to a CSV file.
    
    Args:
        filename (str): The name of the CSV file.
    
    Returns:
        pandas.DataFrame: The exported data as a DataFrame.
    """
    history = get_assessment_history()
    
    if not history:
        return pd.DataFrame()
    
    # Prepare data for export
    data = []
    
    for assessment in history:
        date = assessment["date"]
        scores = assessment["scores"]
        
        row = {
            "Date": date,
            "Overall Score": scores.get("overall", None)
        }
        
        # Add category scores
        for category_id, category in CATEGORIES.items():
            row[f"{category['name']} Score"] = scores.get(category_id, None)
        
        # Add individual question responses
        responses = assessment["responses"]
        for category_id, category in CATEGORIES.items():
            for question in category["questions"]:
                question_id = question["id"]
                response = responses.get(question_id, "NA")
                row[f"{category['name']} - {question['text']}"] = response
        
        data.append(row)
    
    # Create and return DataFrame
    df = pd.DataFrame(data)
    return df

def import_from_csv(uploaded_file):
    """
    Import assessment history from a CSV file.
    
    Args:
        uploaded_file: The uploaded CSV file.
    
    Returns:
        bool: True if import was successful, False otherwise.
    """
    try:
        df = pd.read_csv(uploaded_file)
        
        # Clear existing history
        st.session_state.assessment_history = []
        
        # Extract all question IDs
        all_question_ids = get_all_question_ids()
        
        # Process each row in the DataFrame
        for _, row in df.iterrows():
            date = row["Date"]
            
            # Extract responses
            responses = {}
            for category_id, category in CATEGORIES.items():
                for question in category["questions"]:
                    question_id = question["id"]
                    column_name = f"{category['name']} - {question['text']}"
                    if column_name in row:
                        responses[question_id] = row[column_name]
            
            # Calculate scores
            scores = calculate_scores(responses)
            
            # Save assessment
            assessment = {
                "date": date,
                "responses": responses,
                "scores": scores
            }
            
            st.session_state.assessment_history.append(assessment)
        
        return True
    
    except Exception as e:
        st.error(f"Error importing data: {str(e)}")
        return False
