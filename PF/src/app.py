# # app.py
# import streamlit as st
# from data_processing import preprocess_and_categorize, extract_data_from_pdf
# import pandas as pd

# st.title('Personal Finance Analysis')

# # File Upload Widget
# st.subheader('Upload Your Financial Data (PDF only)')
# uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

# if uploaded_file is not None:
#     # Check the file type
#     file_extension = uploaded_file.name.split('.')[-1]
#     if file_extension == 'pdf':
#         pdf_data = extract_data_from_pdf(uploaded_file)
#         df = preprocess_and_categorize(pdf_data)

#         # Calculate profit/loss and bank balance
#         income_categories = ['Salary', 'Other Income']
#         expenses_categories = ['Housing', 'Food', 'Utilities', 'Transportation', 'Entertainment', 'Other']

#         df['Income'] = df[df['Category'].isin(income_categories)]['Amount']
#         df['Expenses'] = df[df['Category'].isin(expenses_categories)]['Amount']
#         df['Profit/Loss'] = df['Income'].sum() - df['Expenses'].sum()

#         df['Bank Balance'] = df['Amount'].cumsum()

#         # Display the preprocessed data and financial metrics
#         st.subheader('Preprocessed Data')
#         st.write(df)

#         # Display financial metrics
#         st.subheader('Financial Metrics')
#         st.write('Total Income:', df['Income'].sum())
#         st.write('Total Expenses:', df['Expenses'].sum())
#         st.write('Profit/Loss:', df['Profit/Loss'])
#         st.write('Bank Balance:', df['Bank Balance'].iloc[-1])
#     else:
#         st.error('Please upload a PDF file for processing.')


# app.py
import streamlit as st
from data_processing import preprocess_and_categorize, extract_data_from_pdf
import pandas as pd

st.title('Personal Finance Analysis')

# File Upload Widget
st.subheader('Upload Your Financial Data (PDF only)')
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Check the file type
    file_extension = uploaded_file.name.split('.')[-1]
    if file_extension == 'pdf':
        pdf_data = extract_data_from_pdf(uploaded_file)
        df = preprocess_and_categorize(pdf_data)

        # Calculate profit/loss and bank balance
        income_categories = ['Salary', 'Other Income']
        expenses_categories = ['Housing', 'Food', 'Utilities', 'Transportation', 'Entertainment', 'Other']

        df['Income'] = df[df['Category'].isin(income_categories)]['Amount']
        df['Expenses'] = df[df['Category'].isin(expenses_categories)]['Amount']
        df['Profit/Loss'] = df['Income'].sum() - df['Expenses'].sum()

        df['Bank Balance'] = df['Amount'].cumsum()

        # Display the preprocessed data and financial metrics
        st.subheader('Preprocessed Data')
        st.write(df)

        # Display financial metrics
        st.subheader('Financial Metrics')
        st.write('Total Income:', df['Income'].sum())
        st.write('Total Expenses:', df['Expenses'].sum())
        st.write('Profit/Loss:', df['Profit/Loss'])
        st.write('Bank Balance:', df['Bank Balance'].iloc[-1])
    else:
        st.error('Please upload a PDF file for processing.')
