# # data_processing.py
# import pandas as pd
# from PyPDF2 import PdfReader

# def extract_data_from_pdf(pdf_file):
#     pdf_data = []
#     pdf_reader = PdfReader(pdf_file)

#     for page in pdf_reader.pages:
#         page_text = page.extract_text()
#         pdf_data.append(page_text)

#     return pdf_data

# def preprocess_and_categorize(pdf_data):
#     # Perform data preprocessing and categorization as needed
#     # This function can be extended based on your data and categorization logic
#     # Example logic for categorization is given here

#     data = pd.DataFrame({'Description': pdf_data})
#     data['Amount'] = data['Description'].str.extract(r'(\d+\.\d+)').astype(float)
    
#     data['Category'] = data['Description'].apply(categorize_expense)
    
#     # You can add more preprocessing and categorization logic as required
    
#     return data

# def categorize_expense(description):
#     # Implement your logic to categorize expenses here
#     # Example: Categorize as 'Housing' if 'rent' is in the description
#     if "rent" in description.lower():
#         return "Housing"
#     elif "groceries" in description.lower():
#         return "Food"
#     else:
#         return "Other"



# data_processing.py
import pandas as pd
from PyPDF2 import PdfReader

def extract_data_from_pdf(pdf_file):
    pdf_data = []
    pdf_reader = PdfReader(pdf_file)

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        pdf_data.append(page_text)

    return pdf_data

def preprocess_and_categorize(pdf_data):
    # Perform data preprocessing and categorization as needed
    # This function can be extended based on your data and categorization logic
    # Example logic for categorization is given here

    data = pd.DataFrame({'Description': pdf_data})
    data['Amount'] = data['Description'].str.extract(r'(\d+\.\d+)').astype(float)
    
    data['Category'] = data['Description'].apply(categorize_expense)
    
    # You can add more preprocessing and categorization logic as required
    
    return data

def categorize_expense(description):
    # Implement your logic to categorize expenses here
    # Example: Categorize as 'Housing' if 'rent' is in the description
    if "rent" in description.lower():
        return "Housing"
    elif "groceries" in description.lower():
        return "Food"
    else:
        return "Other"
