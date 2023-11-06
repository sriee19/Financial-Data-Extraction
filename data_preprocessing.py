import fitz  # Import PyMuPDF
import pandas as pd

def extract_data_from_pdf(pdf_file):
    pdf_data = []
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        page_text = page.get_text("text")
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
    elif "Zomato" in description.lower():
        return "Food"
    elif "Online Payment" in description.lower():
        return "Food"
    else:
        return "Other"

