"""
Module for managing assessment history and trend analysis.
"""

import pandas as pd
import streamlit as st
import datetime
from categories import CATEGORIES
from data_manager import get_assessment_history, export_to_csv, import_from_csv

def display_history_section():
    """Display the assessment history section."""
    st.header("Assessment History")
    
    history = get_assessment_history()
    
    if not history:
        st.info("No assessment history available. Complete an assessment to see history.")
        return
    
    # Create tabs for different history views
    tab1, tab2, tab3 = st.tabs(["History Table", "Export/Import", "Time Analysis"])
    
    with tab1:
        display_history_table(history)
    
    with tab2:
        handle_export_import()
    
    with tab3:
        display_time_analysis(history)

def display_history_table(history):
    """
    Display the assessment history as a table.
    
    Args:
        history (list): List of assessment dictionaries.
    """
    # Prepare data for the table
    data = []
    
    for assessment in history:
        date = assessment["date"]
        scores = assessment["scores"]
        
        row = {
            "Date": date,
            "Overall Score": f"{scores.get('overall', 'N/A'):.2f}" if scores.get('overall') is not None else "N/A"
        }
        
        # Add category scores
        for category_id, category in CATEGORIES.items():
            category_score = scores.get(category_id)
            row[f"{category['name']} Score"] = f"{category_score:.2f}" if category_score is not None else "N/A"
        
        data.append(row)
    
    # Create and display DataFrame
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

def handle_export_import():
    """Handle export and import of assessment history."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Export History")
        if st.button("Export to CSV"):
            df = export_to_csv()
            if not df.empty:
                # Convert DataFrame to CSV for download
                csv = df.to_csv(index=False).encode('utf-8')
                
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="maturity_assessment_history.csv",
                    mime="text/csv"
                )
            else:
                st.info("No data to export.")
    
    with col2:
        st.subheader("Import History")
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
        
        if uploaded_file is not None:
            if st.button("Import CSV"):
                success = import_from_csv(uploaded_file)
                if success:
                    st.success("Assessment history imported successfully!")
                    st.rerun()

def display_time_analysis(history):
    """
    Display time analysis of assessment scores.
    
    Args:
        history (list): List of assessment dictionaries.
    """
    st.subheader("Score Trends Over Time")
    
    if len(history) < 2:
        st.info("At least two assessments are needed to show trends. Complete more assessments to see trend analysis.")
        return
    
    # Prepare data for trend analysis
    dates = []
    overall_scores = []
    category_scores = {category_id: [] for category_id in CATEGORIES.keys()}
    
    for assessment in history:
        date = assessment["date"]
        scores = assessment["scores"]
        
        dates.append(date)
        overall_scores.append(scores.get("overall", None))
        
        for category_id in CATEGORIES.keys():
            category_scores[category_id].append(scores.get(category_id, None))
    
    # Create DataFrame for trend analysis
    data = {"Date": dates, "Overall": overall_scores}
    for category_id, category in CATEGORIES.items():
        data[category["name"]] = category_scores[category_id]
    
    trend_df = pd.DataFrame(data)
    
    # Convert date string to datetime for proper sorting
    trend_df["Date"] = pd.to_datetime(trend_df["Date"])
    trend_df = trend_df.sort_values("Date")
    
    # Display trend analysis
    st.line_chart(trend_df.set_index("Date").drop(columns=["Overall"]))
    
    # Show improvement areas
    if len(history) >= 2:
        st.subheader("Improvement Analysis")
        
        latest = history[-1]["scores"]
        previous = history[-2]["scores"]
        
        improved = []
        declined = []
        
        for category_id, category in CATEGORIES.items():
            latest_score = latest.get(category_id)
            previous_score = previous.get(category_id)
            
            if latest_score is not None and previous_score is not None:
                difference = latest_score - previous_score
                
                if difference > 0.5:
                    improved.append((category["name"], difference))
                elif difference < -0.5:
                    declined.append((category["name"], difference))
        
        if improved:
            st.success("Most improved areas:")
            for category, diff in sorted(improved, key=lambda x: x[1], reverse=True):
                st.write(f"- {category}: +{diff:.2f} points")
        
        if declined:
            st.warning("Areas needing attention:")
            for category, diff in sorted(declined, key=lambda x: x[1]):
                st.write(f"- {category}: {diff:.2f} points")
        
        if not improved and not declined:
            st.info("No significant changes detected between the last two assessments.")
