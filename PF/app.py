import streamlit as st
import pandas as pd

# Load the categorized data
categorized_data = pd.read_csv('categorized_bank_statement.csv')

# Streamlit UI
st.title("Personal Finance Expense Categorization")
st.write(categorized_data)

# You can add filters, charts, and more to visualize the data
