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

    # Display financial metrics
    st.subheader('Financial Metrics')
    st.write('Bank Balance:', df['Bank Balance'].iloc[-1])

    # Calculate and display the closing balance
    closing_balance = df['Bank Balance'].iloc[-1]
    st.write('Closing Balance:', closing_balance)


    # Display higher expenses and lower spendings in separate tables
    higher_expenses = df[df['Amount'] > 100]
    lower_spendings = df[df['Amount'] < 100]

    st.subheader('Higher Expenses')
    st.write(higher_expenses)

    st.subheader('Lower Spendings')
    st.write(lower_spendings)

    # Bar chart to visualize expenses by category
    st.subheader('Expense Category Breakdown')
    category_expenses = df.groupby('Category')['Amount'].sum().reset_index()
    fig = px.bar(category_expenses, x='Category', y='Amount', labels={'Amount': 'Expense Amount'}, title='Expense Category Breakdown')
    st.plotly_chart(fig)
