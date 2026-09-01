#import libraries
import pandas as pd
import streamlit as st
import plotly.express as px

#set up config
st.set_page_config(
  page_title="Employee Dashboard",
  page_icon="👥",
  layout="wide"
)

@st.cache_data
def load_dataset():
  try:
    df = pd.read_csv("employee_cleaned_dataset.csv")
    return df
  except FileNotFoundError as e:
    st.warning(f"An error occured: {e}")


def create_sidebar_filters(df):
  st.sidebar.header("👥 Employee Filters")
  
  department = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
  )
  
  location = st.sidebar.multiselect(
    "Select Location",
    options=df["Office Location"].unique(),
    default=df["Office Location"].unique()
  )
  
  remote = st.sidebar.radio(
    "Select Remote(s)",
    options=["All", "Yes", " No"],
    index=0
  )
  
  return department, location, remote




def main():
  #load dataset
  df = load_dataset()
  
  #sidebar
  department, location, remote = create_sidebar_filters(df)

if __name__ == "__main__":
  main()