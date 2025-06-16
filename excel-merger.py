# pip install openpyxl
import pandas as pd
import streamlit as st
import zipfile
import base64
import os

# Web App Title
st.markdown('''
# **Excel File Merger**

This is the **Excel File Merger App** created in Python using the Streamlit library.

---
''')

# Excel file merge function
def excel_file_merge(zip_file_name):
    df_list = []
    archive = zipfile.ZipFile(zip_file_name, 'r')

    with archive as f:
        for file in f.namelist():
            if file.endswith('.xlsx'):
                xlfile = archive.open(file)
                df_xl = pd.read_excel(xlfile, engine='openpyxl')
                df_xl['Note'] = file  # Annotate source file
                df_list.append(df_xl)  # Collect dataframes

    return pd.concat(df_list, ignore_index=True) if df_list else pd.DataFrame()

# Upload CSV data
with st.sidebar.header('1. Upload your ZIP file'):
    uploaded_file = st.sidebar.file_uploader("Excel-containing ZIP file", type=["zip"])
    st.sidebar.markdown("""
[Example ZIP input file](https://github.com/dataprofessor/excel-file-merge-app/raw/main/nba_data.zip)
""")

# File download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="merged_file.csv">Download Merged File as CSV</a>'
    return href

def xldownload(df):
    df.to_excel('data.xlsx', index=False)
    data = open('data.xlsx', 'rb').read()
    b64 = base64.b64encode(data).decode('UTF-8')
    #b64 = base64.b64encode(xl.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/xls;base64,{b64}" download="merged_file.xlsx">Download Merged File as XLSX</a>'
    return href

# Main panel
if st.sidebar.button('Submit'):
    #@st.cache
    df = excel_file_merge(uploaded_file)
    st.header('**Merged data**')
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)
    st.markdown(xldownload(df), unsafe_allow_html=True)
else:
    st.info('Awaiting for ZIP file to be uploaded.')