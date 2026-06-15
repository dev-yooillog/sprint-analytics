import streamlit as st

st.title("Targeting high-risk groups")
df = st.session_state["df"]

col1, col2 = st.columns(2)
level_filter = col1.multiselect(
    "위험 등급",
    ["High", "Medium", "Low"],
    default=["High", "Medium"],
)
category_filter = col2.multiselect(
    "카테고리",
    df["course_category"].unique().tolist(),
    default=df["course_category"].unique().tolist(),
)

filtered = df[
    df["dropout_risk"].isin(level_filter) &
    df["course_category"].isin(category_filter)
].copy()
filtered = filtered.sort_values("engagement_score", ascending=True)

display_cols = {
    "student_id": "수강생 ID",
    "course_category": "카테고리",
    "dropout_risk": "이탈 위험",
    "engagement_score": "몰입도 점수",
    "course_progress_percent": "진도율 (%)",
    "quiz_average_score": "퀴즈 점수",
    "login_frequency_per_week": "주간 접속 횟수",
    "device_type": "기기",
}

st.dataframe(
    filtered[list(display_cols.keys())].rename(columns=display_cols),
    use_container_width=True,
    hide_index=True,
)
st.caption(
    f"총 {len(filtered)}명 표시 중 · "
    f"High 위험군 전체 {(df['dropout_risk'] == 'High').sum()}명"
)