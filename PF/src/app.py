# app.py
import streamlit as st
from data_processing import preprocess_and_categorize

# Load and preprocess the data
data_path = 'fdata.csv'
df = preprocess_and_categorize(data_path)

st.title('Personal Finance Analysis')

# Display raw data
st.subheader('Raw Data')
st.write(df)

# Create Streamlit widgets for user interaction

# Select box to filter data by expense category
st.subheader('Filter Data by Expense Category')
selected_category = st.selectbox('Select an Expense Category', ['All'] + df['Category'].unique())
if selected_category != 'All':
    filtered_df = df[df['Category'] == selected_category]
else:
    filtered_df = df

st.write('Displaying data for:', selected_category)
st.write(filtered_df)

# Sidebar Date Range Selector
st.sidebar.subheader('Date Range Selector')
start_date = st.sidebar.date_input('Start Date', min_value=df['Date'].min(), max_value=df['Date'].max())
end_date = st.sidebar.date_input('End Date', min_value=df['Date'].min(), max_value=df['Date'].max())

# Filter data based on the selected date range
date_filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

st.subheader('Data for Selected Date Range')
st.write(date_filtered_df)

# Bar chart to visualize expenses by category
st.subheader('Expense Category Breakdown')
category_expenses = df.groupby('Category')['Amount'].sum()
st.bar_chart(category_expenses)

# Display total income, total expenses, profit/loss, and bank balance
st.subheader('Financial Summary')
st.write('Total Income:', df['Income'].sum())
st.write('Total Expenses:', df['Expenses'].sum())
st.write('Profit/Loss:', df['Profit/Loss'].sum())
st.write('Bank Balance:', df['Bank Balance'].iloc[-1])

