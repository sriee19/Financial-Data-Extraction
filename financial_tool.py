import streamlit as st
import pandas as pd
import openai_helper

col1, col2 = st.columns([3,3])

financial_data_df = pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })

with col1:
    st.title("Data Extraction Tool using OpenAI API")
    news_article = st.text_area("Paste your financial article here", height=300)
    if st.button("Extract"):
        financial_data_df = openai_helper.extract_financial_data(news_article)

with col2:
    st.markdown("<br/>" * 5, unsafe_allow_html=True)
    st.dataframe(financial_data_df)  
    
