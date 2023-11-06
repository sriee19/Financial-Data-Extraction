
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

    # Calculate expenses
    expenses_categories = ['House','Shop','Food','Shopping','Study','Payback','Drinks','Snacks']
    df['Expenses'] = df[df['Category'].isin(expenses_categories)]['Amount']

    df['Bank Balance'] = df['Amount'].cumsum()

    # Display the preprocessed data and financial metrics
    st.subheader('Preprocessed Data')
    st.write(df)

    # Display financial metrics
    st.subheader('Financial Metrics')
    st.write('Total Expenses:', df['Expenses'].sum())
    st.write('Bank Balance:', df['Bank Balance'].iloc[-1])

    # Line chart to visualize bank balance over time
    st.subheader('Bank Balance Over Time (Resampled)')
    balance_fig = px.line(df, x=df.index, y='Bank Balance', labels={'Bank Balance': 'Balance'}, title='Bank Balance Over Time')
    balance_fig.update_xaxes(title_text='Date')
    balance_fig.update_yaxes(title_text='Balance')
    st.plotly_chart(balance_fig)
