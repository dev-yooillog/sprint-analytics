import pandas as pd

def load_data(path: str = "data/online_learning_engagement_dropout_risk.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df["dropout_risk"] = pd.Categorical(
        df["dropout_risk"], categories=["Low", 
                                        "Medium", 
                                        "High"], ordered=True
    )
    return df