import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(page_title="Student Dashboard", layout="wide")

st.title(" Student Performance Dashboard")
# SIDEBAR FILTERS
st.sidebar.header("Filter Students")

num_students = st.sidebar.slider("Number of Students", 10, 200, 50)
subject = st.sidebar.selectbox("Select Subject", ["Math", "Science", "English"])

# CREATE SAMPLE DATA
data = pd.DataFrame({
    "Name": [f"Student {i}" for i in range(num_students)],
    "Math": np.random.randint(40, 100, num_students),
    "Science": np.random.randint(40, 100, num_students),
    "English": np.random.randint(40, 100, num_students),
})

# SHOW DATA
st.subheader("📋 Student Data")
st.dataframe(data)

# METRICS (TOP CARDS)
# -------------------------------
avg_score = int(data[subject].mean())
max_score = int(data[subject].max())
min_score = int(data[subject].min())

col1, col2, col3 = st.columns(3)

col1.metric("Average Score", avg_score)
col2.metric("Highest Score", max_score)
col3.metric("Lowest Score", min_score)

# CHARTS
st.subheader(f" {subject} Analysis")

col4, col5 = st.columns(2)

# Histogram
with col4:
    st.write("Score Distribution")
    fig, ax = plt.subplots()
    ax.hist(data[subject])
    st.pyplot(fig)

# Line Chart
with col5:
    st.write("Scores Trend")
    fig2, ax2 = plt.subplots()
    ax2.plot(data[subject])
    ax2.set_xlabel("Students")
    ax2.set_ylabel("Score")
    st.pyplot(fig2)

# TOP PERFORMERS
st.subheader("🏆 Top 5 Students")

top_students = data.sort_values(by=subject, ascending=False).head(5)
st.table(top_students)

# INTERACTION BUTTON
if st.button("Show Insights"):
    st.success(f"Average {subject} score is {avg_score}. Focus on improving low performers.")