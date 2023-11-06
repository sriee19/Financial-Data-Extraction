import streamlit as st
from data_processing import preprocess_and_categorize, extract_data_from_pdf
import pandas as pd
import plotly.express as px
import io  # Import io for BytesIO

st.title('Personal Finance Analysis')

# File Upload Widget
st.subheader('Upload Your Financial Data (PDF only)')
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    pdf_data = extract_data_from_pdf(uploaded_file)
    df = preprocess_and_categorize(pdf_data)

    # Calculate profit/loss and bank balance
    income_categories = ['Salary', 'Other Income']
    expenses_categories = ['Housing', 'Food', 'Utilities', 'Transportation', 'Entertainment', 'Other']

    df['Income'] = df[df['Category'].isin(income_categories)]['Amount']
    df['Expenses'] = df[df['Category'].isin(expenses_categories)]['Amount']
    df['Bank Balance'] = df['Amount'].cumsum()

    # Display the preprocessed data and financial metrics
    st.subheader('Preprocessed Data')
    st.write(df)

    # Display financial metrics
    st.subheader('Financial Metrics')
    st.write('Total Income:', df['Income'].sum())
    st.write('Total Expenses:', df['Expenses'].sum())
    st.write('Bank Balance:', df['Bank Balance'].iloc[-1])

 # Line chart to visualize balance over time
st.subheader('Bank Balance Over Time (Resampled)')

# Make sure 'Date' is a datetime column in your DataFrame
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the DataFrame index
df.set_index('Date', inplace=True)

# Resample the data
balance_resampled = df.resample('D').asfreq()
balance_resampled['Bank Balance'] = balance_resampled['Bank Balance'].fillna(method='ffill')

# Create a line chart
balance_fig = px.line(balance_resampled, x=balance_resampled.index, y='Bank Balance', labels={'Bank Balance': 'Balance'}, title='Bank Balance Over Time (Daily)')
balance_fig.update_xaxes(title_text='Date')
balance_fig.update_yaxes(title_text='Balance')
st.plotly_chart(balance_fig)


