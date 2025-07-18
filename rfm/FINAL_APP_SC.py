import subprocess

try:
    import matplotlib
    print("✅ matplotlib version:", matplotlib.__version__)
except ImportError:
    print("❌ matplotlib not found")

# List all installed packages in logs
subprocess.run(["pip", "list"])



import streamlit as st
import pandas as pd
import matplotlib
# matplotlib.use('Agg')  # Set backend before importing pyplot
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="RFM Dashboard", layout="wide")
st.title("Employee Engagement RFM Dashboard")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("RFM_DEPLOY.csv")

# Load the data
rfm = load_data()

# Show Data
if st.checkbox("Show RFM Data"):
    st.dataframe(rfm)

# Cluster Counts
st.subheader("Cluster Distribution")
if 'Cluster' in rfm.columns:
    cluster_counts = rfm['Cluster'].value_counts().sort_index()
    st.bar_chart(cluster_counts)
else:
    st.warning("No 'Cluster' column found in the dataset.")

# PCA Cluster Plot
st.subheader("Cluster Visualization")
if 'PCA1' in rfm.columns and 'PCA2' in rfm.columns:
    fig, ax = plt.subplots()
    sns.scatterplot(data=rfm, x='PCA1', y='PCA2', hue='Cluster', palette='Set2', s=80, ax=ax)
    st.pyplot(fig)
else:
    st.warning("PCA1 or PCA2 columns not found in the dataset.")
