import pandas as pd

# Load the bank statement data (replace with your data source)
df = pd.read_csv('bank_statement.csv')

# Define a function to categorize expenses
def categorize_expense(description):
    # Implement your logic to categorize expenses here
    # You can use if-else statements or regex patterns
    if "rent" in description.lower():
        return "Housing"
    elif "groceries" in description.lower():
        return "Food"
    else:
        return "Other"

# Apply the categorization function to the 'Description' column
df['Category'] = df['Description'].apply(categorize_expense)

# Save the categorized data to a new CSV file
df.to_csv('categorized_bank_statement.csv', index=False)
