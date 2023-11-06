# Import the required libraries
import streamlit as st
from data_processing import preprocess_and_categorize, extract_data_from_pdf
import pandas as pd
import plotly.express as px

st.title('Personal Finance Analysis')

# File Upload Widget
st.subheader('Upload Your Financial Data (PDF only)')
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    pdf_data = extract_data_from_pdf(uploaded_file)
    df = preprocess_and_categorize(pdf_data)

    # Calculate bank balance
    df['Bank Balance'] = df['Amount'].cumsum()

    # Display the preprocessed data and financial metrics
    st.subheader('Preprocessed Data')
    st.write(df)

    # Create a line graph for both higher expenses and lower spendings
    higher_expenses = df[df['Amount'] > 100]
    lower_spendings = df[df['Amount'] < 100]

    higher_expenses['Type'] = 'Higher Expenses'
    lower_spendings['Type'] = 'Lower Spendings'
    combined_df = pd.concat([higher_expenses, lower_spendings])

    line_fig = px.line(combined_df, x=combined_df.index, y='Amount', labels={'Amount': 'Expense Amount'}, 
                      title='Expense Over Time for Higher Expenses and Lower Spendings', color='Type')

    # Create a line graph for bank balance over time
    balance_fig = px.line(df, x=df.index, y='Bank Balance', labels={'Bank Balance': 'Balance'},
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
