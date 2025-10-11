import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set up the page layout and title
st.set_page_config(page_title="Data Visualization App", layout="wide")
st.title("Interactive Data Visualization")

# Sidebar for User Input
st.sidebar.header("User Inputs")
chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot"])
color = st.sidebar.color_picker("Pick a Color", "#00f900")

# Generate sample data
np.random.seed(42)
data = pd.DataFrame({
    "Category": ['A', 'B', 'C', 'D', 'E'],
    "Value": np.random.randint(1, 100, 5),
    "Sales": np.random.randint(100, 1000, 5),
    "Revenue": np.random.randint(2000, 5000, 5)
})

# Display the data table
st.subheader("Data Table")
st.dataframe(data)

# Visualization
st.subheader("Visualization")

if chart_type == "Bar Chart":
    # Bar chart
    st.write(f"Displaying a Bar Chart with {color} color.")
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Category", y="Value", data=data, palette=[color])
    plt.title("Bar Chart of Categories")
    st.pyplot()

elif chart_type == "Line Chart":
    # Line chart
    st.write(f"Displaying a Line Chart with {color} color.")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="Category", y="Sales", data=data, marker='o', color=color)
    plt.title("Line Chart of Sales")
    st.pyplot()

elif chart_type == "Scatter Plot":
    # Scatter plot
    st.write(f"Displaying a Scatter Plot with {color} color.")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Sales", y="Revenue", data=data, color=color, s=100)
    plt.title("Scatter Plot of Sales vs Revenue")
    st.pyplot()

# Footer Information
st.markdown("---")
st.markdown("Created by Ahmed Ismail for Data Visualization.")
