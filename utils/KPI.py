import pandas as pd

W_SESSION = 0.4
W_PROGRESS = 0.6

def engagement_score(df: pd.DataFrame) -> pd.Series:
    session_norm = df["avg_session_minutes"] / df["avg_session_minutes"].max()
    score = (session_norm * W_SESSION + df["course_progress_percent"] / 100 * W_PROGRESS) * 100
    return score.round(1)

def dropout_risk_score(df: pd.DataFrame) -> pd.Series:
    mapping = {"Low": 0, "Medium": 50, "High": 100}
    return df["dropout_risk"].map(mapping)