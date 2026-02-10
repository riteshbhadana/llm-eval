import streamlit as st
import json
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="LLM Evaluation Platform",
    layout="wide"
)

st.title("🚀 LLM Evaluation Platform")
st.caption("Automated regression & quality monitoring for LLM outputs")

if not os.path.exists("runs/results.json"):
    st.warning("No evaluation results found. Run `python run_eval.py` first.")
    st.stop()

with open("runs/results.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ---------- Metrics Row ----------
col1, col2, col3 = st.columns(3)

col1.metric("Average Score", round(df["score"].mean(), 2))
col2.metric("Best Score", df["score"].max())
col3.metric("Worst Score", df["score"].min())

st.divider()

# ---------- Chart ----------
fig = px.bar(
    df,
    x="id",
    y="score",
    title="Evaluation Scores per Test Case",
    text="score"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------- Table ----------
st.subheader("Detailed Results")
st.dataframe(df, use_container_width=True)

# ---------- Insights ----------
st.subheader("Insights")

if df["score"].mean() < 5:
    st.error("⚠️ Severe performance issue.")
elif df["score"].mean() < 7:
    st.warning("⚠️ Moderate performance.")
else:
    st.success("✅ Model performing well.")
