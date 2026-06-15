import streamlit as st
import pandas as pd
from utils.preprocess import load_data
from utils.KPI import engagement_score, dropout_risk_score

st.set_page_config(
    page_title="Sprint Analytics",
    page_icon="",
    layout="wide",
)

@st.cache_data
def get_data():
    df = load_data()
    df["engagement_score"] = engagement_score(df)
    df["dri_score"] = dropout_risk_score(df)
    return df

df = get_data()
st.session_state["df"] = df

st.title("Sprint Analytics")
st.caption("Online Learning Engagement Dataset 기반 학습 성과 모니터링 시스템")

total = len(df)
high_risk = (df["dropout_risk"] == "High").sum()
completion_rate = round((1 - high_risk / total) * 100, 1)
avg_progress = round(df["course_progress_percent"].mean(), 1)
avg_dri = round(high_risk / total * 100, 1)
avg_engagement = round(df["engagement_score"].mean(), 1)

col1, col2, col3, col4 = st.columns(4)
col1.metric("완주 예상률", f"{completion_rate}%")
col2.metric("평균 진도율", f"{avg_progress}%")
col3.metric("위험군 비율 (High)", f"{avg_dri}%")
col4.metric("평균 몰입도 점수", str(avg_engagement))