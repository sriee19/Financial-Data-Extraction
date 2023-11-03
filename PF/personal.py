import pandas as pd

# Load the bank statement data (replace with your data source)
df = pd.read_csv('fdata.csv')

# Define a function to categorize expenses
def categorize_expense(description):
    # Convert the description to lowercase for case-insensitive matching
    description = description.lower()

    # Define your categorization logic using if-else statements or regex patterns
    if "rent" in description:
        return "Housing"
    elif "groceries" in description:
        return "Food"
    elif "dining" in description or "restaurant" in description:
        return "Dining Out"
    elif "utility" in description:
        return "Utilities"
    else:
        return "Other"

# Apply the categorization function to the 'Description' column
df['Category'] = df['Description'].apply(categorize_expense)

# Save the categorized data to a new CSV file
df.to_csv('categorized_bank_statement.csv', index=False)
