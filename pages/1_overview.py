import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.title("Overview Dashboard")
df = st.session_state["df"]

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

st.divider()

col_a, col_b = st.columns([1, 2])

with col_a:
    risk_counts = df["dropout_risk"].value_counts().reindex(["Low", "Medium", "High"])
    fig = go.Figure(go.Pie(
        values=risk_counts.values,
        labels=risk_counts.index,
        hole=0.65,
        marker_colors=["#3DD68C", "#FF9F43", "#FF6B6B"],
        textinfo="none",
    ))
    fig.update_layout(
        showlegend=True,
        height=280,
        margin=dict(t=20, b=20, l=20, r=20),
        annotations=[dict(text=f"{completion_rate}%", font_size=24, showarrow=False)],
    )
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    cat_avg = (
        df.groupby("course_category")["course_progress_percent"]
        .mean()
        .reset_index()
        .sort_values("course_progress_percent", ascending=False)
    )
    fig2 = px.bar(
        cat_avg,
        x="course_category",
        y="course_progress_percent",
        color="course_progress_percent",
        color_continuous_scale=["#FF6B6B", "#FF9F43", "#3DD68C"],
        labels={
            "course_category": "카테고리",
            "course_progress_percent": "평균 진도율 (%)",
        },
        title="카테고리별 평균 진도율",
    )
    fig2.update_layout(coloraxis_showscale=False, height=280)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("몰입도 점수의 분포")
fig3 = px.histogram(
    df,
    x="engagement_score",
    color="dropout_risk",
    color_discrete_map={"Low": "#3DD68C", "Medium": "#FF9F43", "High": "#FF6B6B"},
    nbins=30,
    barmode="overlay",
    opacity=0.7,
    labels={"engagement_score": "몰입도 점수", "dropout_risk": "이탈 위험"},
)
fig3.update_layout(height=280)
st.plotly_chart(fig3, use_container_width=True)