"""
Maturity Assessment Tool
Author: Kiran Kumar
A Streamlit-based application for conducting organizational maturity assessments
across multiple categories, with scoring visualizations and trend analysis.
"""

import streamlit as st
import pandas as pd
import datetime
from categories import CATEGORIES
from data_manager import (
    initialize_session_state,
    save_current_responses,
    get_current_responses,
    calculate_scores,
    save_assessment,
    clear_current_assessment
)
from visualizations import (
    display_category_radar_chart,
    display_score_gauges,
    display_question_responses_chart,
    display_strength_weakness_analysis,
    display_maturity_heatmap
)
from assessment_history import display_history_section

# Set up page configuration
st.set_page_config(
    page_title="Maturity Assessment Tool",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
initialize_session_state()

# App title and description
st.title("Organizational Maturity Assessment Tool")
st.markdown("""
This tool helps you evaluate your organization's maturity across different categories.
Complete the assessment to see your strengths and areas for improvement.
""")

# Main navigation
tab1, tab2, tab3 = st.tabs(["Assessment", "Results", "History"])

# Assessment tab
with tab1:
    st.header("Complete Your Assessment")
    
    # Assessment date input
    st.session_state.assessment_date = st.date_input(
        "Assessment Date",
        datetime.datetime.strptime(st.session_state.assessment_date, "%Y-%m-%d").date()
    ).strftime("%Y-%m-%d")
    
    # Get current responses
    responses = get_current_responses()
    
    # Display assessment questions by category
    for category_id, category in CATEGORIES.items():
        with st.expander(f"{category['name']} - {category['description']}", expanded=True):
            st.write(f"### {category['name']}")
            st.write(category['description'])
            
            for question in category["questions"]:
                question_id = question["id"]
                
                # Display the question with tooltip if maturity hints are available
                if "maturity_hints" in question:
                    # Create tooltip content
                    tooltip_text = ""
                    if question["type"] == "likert":
                        for level in range(6):  # 0 to 5
                            tooltip_text += f"**Level {level}**: {question['maturity_hints'][level]}\n\n"
                    else:
                        tooltip_text += f"**Yes**: {question['maturity_hints']['Yes']}\n\n"
                        tooltip_text += f"**No**: {question['maturity_hints']['No']}\n\n"
                    
                    # Initialize tooltip state if not exists
                    tooltip_key = f"tooltip_{question['id']}"
                    if tooltip_key not in st.session_state:
                        st.session_state[tooltip_key] = False
                    
                    # Create a row with question and info button
                    col1, col2 = st.columns([0.95, 0.05])
                    with col1:
                        st.markdown(f"**{question['text']}**")
                    with col2:
                        if st.button("ℹ️", key=f"hint_btn_{question['id']}"):
                            st.session_state[tooltip_key] = not st.session_state[tooltip_key]
                    
                    # Show tooltip content if toggle is on
                    if st.session_state[tooltip_key]:
                        st.info(tooltip_text)
                else:
                    st.write(f"**{question['text']}**")
                
                # Handle different question types
                if question["type"] == "likert":
                    # Likert scale questions (0-5)
                    options = ["Not Applicable", "0", "1", "2", "3", "4", "5"]
                    help_text = "0 = Not implemented, 5 = Fully implemented and optimized"
                    
                    # Map "NA" in responses to "Not Applicable" for display
                    index_value = 0
                    if question_id in responses:
                        if responses[question_id] == "NA":
                            index_value = 0  # Index of "Not Applicable"
                        else:
                            index_value = options.index(responses[question_id])
                    
                    response = st.radio(
                        f"Response for {question_id}",
                        options,
                        index=index_value,
                        key=f"radio_{question_id}",
                        help=help_text,
                        horizontal=True,
                        label_visibility="collapsed"
                    )
                else:
                    # Binary questions (Yes/No)
                    options = ["Not Applicable", "Yes", "No"]
                    help_text = "Yes = Implemented (score: 5), No = Not implemented (score: 0)"
                    
                    # Map "NA" in responses to "Not Applicable" for display
                    index_value = 0
                    if question_id in responses:
                        if responses[question_id] == "NA":
                            index_value = 0  # Index of "Not Applicable"
                        else:
                            index_value = options.index(responses[question_id])
                    
                    response = st.radio(
                        f"Response for {question_id}",
                        options,
                        index=index_value,
                        key=f"radio_{question_id}",
                        help=help_text,
                        horizontal=True,
                        label_visibility="collapsed"
                    )
                
                # Store the response
                if response == "Not Applicable":
                    responses[question_id] = "NA"
                else:
                    responses[question_id] = response
                
                st.divider()
            
    # Save responses
    save_current_responses(responses)
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("Calculate Scores", type="primary"):
            # Calculate scores
            scores = calculate_scores(responses)
            st.session_state.current_scores = scores
            
            # Navigate to results tab
            st.rerun()
    
    with col2:
        if st.button("Save Assessment"):
            if len(responses) > 0:
                # Calculate scores
                scores = calculate_scores(responses)
                
                # Save assessment
                save_assessment(responses, scores, st.session_state.assessment_date)
                
                st.success("Assessment saved successfully!")
                clear_current_assessment()
                st.rerun()
            else:
                st.warning("Please complete at least one question before saving.")
    
    with col3:
        if st.button("Clear Assessment"):
            clear_current_assessment()
            st.rerun()

# Results tab
with tab2:
    st.header("Assessment Results")
    
    # Check if scores are available
    if hasattr(st.session_state, 'current_scores'):
        scores = st.session_state.current_scores
        responses = get_current_responses()
        
        # Display overall score prominently
        if "overall" in scores and scores["overall"] is not None:
            st.metric("Overall Maturity Score", f"{scores['overall']:.2f}/5.00")
            
            # Create columns for key insights
            col1, col2 = st.columns(2)
            
            with col1:
                # Radar chart of category scores
                display_category_radar_chart(scores)
            
            with col2:
                # Maturity heatmap
                display_maturity_heatmap(scores)
            
            # Score gauges
            display_score_gauges(scores)
            
            # Question responses chart
            display_question_responses_chart(responses)
            
            # Strengths and weaknesses analysis
            display_strength_weakness_analysis(scores, responses)
            
            # Recommendations
            st.subheader("Next Steps")
            st.info("""
            Based on your assessment results:
            1. Focus on improving the lowest-scoring categories
            2. Create an action plan for addressing specific improvement opportunities
            3. Re-assess regularly to track progress
            4. Share results with stakeholders to align improvement efforts
            """)
        else:
            st.info("Complete the assessment to see your results.")
    else:
        st.info("Complete the assessment in the Assessment tab to see your results here.")

# History tab
with tab3:
    display_history_section()

# Footer
st.markdown("---")
st.markdown("© 2023 Maturity Assessment Tool | Developed with Streamlit")
