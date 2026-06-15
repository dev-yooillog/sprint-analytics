import streamlit as st
import plotly.express as px

st.title("Learning Bottleneck Analysis")
df = st.session_state["df"]

bottleneck = (
    df.groupby("course_category")
    .agg(
        high_risk_ratio=("dropout_risk", lambda x: (x == "High").mean() * 100),
        avg_quiz=("quiz_average_score", "mean"),
        avg_progress=("course_progress_percent", "mean"),
        avg_session=("avg_session_minutes", "mean"),
        count=("student_id", "count"),
    )
    .reset_index()
    .sort_values("high_risk_ratio", ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(
        bottleneck,
        x="course_category",
        y="high_risk_ratio",
        color="high_risk_ratio",
        color_continuous_scale=["#3DD68C", "#FF9F43", "#FF6B6B"],
        title="카테고리별 High 위험군 비율 (%)",
        labels={
            "high_risk_ratio": "위험군 비율 (%)",
            "course_category": "카테고리",
        },
    )
    fig.update_layout(coloraxis_showscale=False, height=320)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.scatter(
        bottleneck,
        x="avg_quiz",
        y="high_risk_ratio",
        size="count",
        text="course_category",
        color="high_risk_ratio",
        color_continuous_scale=["#3DD68C", "#FF6B6B"],
        title="퀴즈 점수 vs 위험군 비율",
        labels={
            "avg_quiz": "평균 퀴즈 점수",
            "high_risk_ratio": "위험군 비율 (%)",
        },
    )
    fig2.update_traces(textposition="top center")
    fig2.update_layout(coloraxis_showscale=False, height=320)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("커리큘럼 개선 제언")
colors = ["#FF6B6B", "#A8D5A2", "#5B7FFF"]
for i, (_, row) in enumerate(bottleneck.head(3).iterrows()):
    color = colors[i]
    st.markdown(
        f"""
        <div style="
            background-color: {color}18;
            border: 1px solid {color}55;
            border-radius: 10px;
            padding: 18px 22px;
            margin-bottom: 12px;
        ">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
                <span style="
                    background-color:{color}33;
                    color:{color};
                    font-weight:700;
                    font-size:13px;
                    padding: 3px 10px;
                    border-radius:20px;
                ">#{i+1}</span>
                <span style="color:{color}; font-weight:700; font-size:16px;">
                    {row['course_category']}
                </span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:8px; margin-bottom:12px;">
                <div style="background:#ffffff10; border-radius:6px; padding:8px 12px;">
                    <div style="color:#8892A4; font-size:11px; margin-bottom:2px;">High 위험군</div>
                    <div style="color:{color}; font-size:18px; font-weight:700;">{row['high_risk_ratio']:.1f}%</div>
                </div>
                <div style="background:#ffffff10; border-radius:6px; padding:8px 12px;">
                    <div style="color:#8892A4; font-size:11px; margin-bottom:2px;">평균 퀴즈</div>
                    <div style="color:#E8ECF4; font-size:18px; font-weight:700;">{row['avg_quiz']:.1f}점</div>
                </div>
                <div style="background:#ffffff10; border-radius:6px; padding:8px 12px;">
                    <div style="color:#8892A4; font-size:11px; margin-bottom:2px;">평균 진도율</div>
                    <div style="color:#E8ECF4; font-size:18px; font-weight:700;">{row['avg_progress']:.1f}%</div>
                </div>
                <div style="background:#ffffff10; border-radius:6px; padding:8px 12px;">
                    <div style="color:#8892A4; font-size:11px; margin-bottom:2px;">평균 세션</div>
                    <div style="color:#E8ECF4; font-size:18px; font-weight:700;">{row['avg_session']:.0f}분</div>
                </div>
            </div>
    
        </div>
        """,
        unsafe_allow_html=True,
    )

st.subheader("전체 카테고리 상세 지표")
st.dataframe(
    bottleneck.rename(columns={
        "course_category": "카테고리",
        "high_risk_ratio": "위험군 비율 (%)",
        "avg_quiz": "평균 퀴즈 점수",
        "avg_progress": "평균 진도율 (%)",
        "avg_session": "평균 세션 (분)",
        "count": "수강생 수",
    }).round(1),
    use_container_width=True,
    hide_index=True,
)