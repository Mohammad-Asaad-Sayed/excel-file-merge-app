# excel-file-merge-app

# Demo

Launch the web app:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/excel-file-merge-app/main/app.py)

# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *excel*
```
conda create -n excel python=3.7.9
```
Secondly, we will login to the *excel* environement
```
conda activate excel
```
### Install prerequisite libraries

Download requirements.txt file

```
wget https://github.com/Mohammad-Asaad-Sayed/excel-file-merge-app/blob/main/requirements.txt

```

Pip install libraries
```
pip install -r requirements.txt
```

###  Download and unzip contents from GitHub repo

Download and unzip contents from https://github.com/dataprofessor/excel-file-merge-app/archive/main.zip

###  Launch the app

```
streamlit run app.py
```
