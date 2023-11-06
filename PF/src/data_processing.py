

# data_processing.py
import pandas as pd
import re

def extract_data_from_pdf(uploaded_file):
    pdf_data = []

    if uploaded_file is not None:
        pdf_data = uploaded_file.read().decode("utf-8").splitlines()

    return pdf_data

def preprocess_and_categorize(pdf_data):
    # Perform data preprocessing and categorization as needed

    # Initialize empty lists to store data
    descriptions = []
    amounts = []
    categories = []

    # Define your custom categorization logic here
    custom_categories = {
        'Rent': 'Housing',
        'Groceries': 'Food',
        'Utilities': 'Utilities',
        'Transportation': 'Transportation',
        'Entertainment': 'Entertainment',
        # Add more custom categories and keywords as needed
    }

    # Iterate through the extracted PDF data
    for line in pdf_data:
        # Extract description and amount (customize this based on your PDF format)
        description, amount = extract_description_and_amount(line)

        # Categorize expenses based on keywords or patterns in the description
        category = categorize_expense(description, custom_categories)

        # Add data to the lists
        descriptions.append(description)
        amounts.append(amount)
        categories.append(category)

    # Create a DataFrame with the extracted data
    data = pd.DataFrame({'Description': descriptions, 'Amount': amounts, 'Category': categories})

    return data

def extract_description_and_amount(text):
    # Customize this function to extract description and amount based on your PDF format
    description = ""
    amount = None

    # Example: Extract description and amount using regular expressions
    match = re.match(r'^(.*?)(\d+\.\d+)$', text)
    if match:
        description = match.group(1)
        amount = float(match.group(2))

    return description, amount

def categorize_expense(description, custom_categories):
    # Implement your logic to categorize expenses here
    # Default to "Other" if no match is found in custom_categories
    for keyword, custom_category in custom_categories.items():
        if keyword.lower() in description.lower():
            return custom_category
    return "Other"
