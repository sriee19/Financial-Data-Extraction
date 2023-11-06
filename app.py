# Import the required libraries
import streamlit as st
from data_processing import preprocess_and_categorize, extract_data_from_pdf
import pandas as pd
import plotly.express as px
import re

# Function to extract and format the date from descriptions
def extract_and_format_date(description):
    # Regular expression pattern to match a date in the format "YYYY-MM-DD"
    date_pattern = r'\d{2}-\d{2}-\d{4}'
    
    # Find the first date in the description
    match = re.search(date_pattern, description)
    
    if match:
        date = match.group()
        return date
    
    # Return a default date if no date is found
    return "N/A"

# Function to truncate descriptions
def truncate_description(description, max_length=50):
    return description[:max_length] + '...' if len(description) > max_length else description

st.title('Personal Finance Analysis')

# File Upload Widget
st.subheader('Upload Your Financial Data (PDF only)')
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    pdf_data = extract_data_from_pdf(uploaded_file)
    df = preprocess_and_categorize(pdf_data)

    # Calculate bank balance
    df['Bank Balance'] = df['Amount'].cumsum()

    # Add a date column
    df['Date'] = df['Description'].apply(extract_and_format_date)

    # Truncate descriptions for better display
    df['Description'] = df['Description'].apply(truncate_description)

    # Create a line graph for both higher expenses and lower spendings
    higher_expenses = df[df['Amount'] > 200]
    lower_spendings = df[df['Amount'] < 200]

    higher_expenses['Type'] = 'Higher Expenses'
    lower_spendings['Type'] = 'Lower Spendings'
    combined_df = pd.concat([higher_expenses, lower_spendings])

    line_fig = px.line(combined_df, x='Date', y='Amount', labels={'Amount': 'Expense Amount'}, 
                      title='Expense Over Time for Higher Expenses and Lower Spendings', color='Type')

    # Create a line graph for bank balance over time
    balance_fig = px.line(df, x='Date', y='Bank Balance', labels={'Bank Balance': 'Balance'},
                         title='Bank Balance Over Time')

    # Display the table with higher expenses and lower spendings
    st.subheader('Higher Expenses')
    st.write(higher_expenses)

    st.subheader('Lower Spendings')
    st.write(lower_spendings)

    # Display financial metrics
    st.subheader('Financial Metrics')
    st.write('Bank Balance:', df['Bank Balance'].iloc[-1])

    # Calculate and display the closing balance
    closing_balance = df['Bank Balance'].iloc[-1]
    st.write('Closing Balance:', closing_balance)

    # Display the line graph for expenses
    st.subheader('Expense Over Time')
    st.plotly_chart(line_fig)

    # Display the line graph for bank balance
    st.subheader('Bank Balance Over Time')
    st.plotly_chart(balance_fig)
