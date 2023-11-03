import pandas as pd

def preprocess_and_categorize(data_path):
    # Load the data
    df = pd.read_csv('fdata.csv')

    # Categorize expenses based on transaction descriptions
    def categorize_expense(description):
        if "Monthly Credit" in description.lower():
            return "Online payment"
        elif "Other Income" in description.lower():
            return "Entertainment"
        else:
            return "Other"

    df['Category'] = df['Description'].apply(categorize_expense)

    # Calculate profit or loss
    # You can modify this logic based on your income and expense structure
    income_categories = ['Monthly credit', 'Other Income']
    expenses_categories = ['Snacks', 'Food', 'Online payment', 'Entertainment', 'Other']

    df['Income'] = df[df['Category'].isin(income_categories)]['Amount']
    df['Expenses'] = df[df['Category'].isin(expenses_categories)]['Amount']
    df['Profit/Loss'] = df['Income'] - df['Expenses']

    # Calculate bank balance
    df['Bank Balance'] = df['Amount'].cumsum()

    return df

