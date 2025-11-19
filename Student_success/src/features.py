import pandas as pd
import numpy as np
from datetime import datetime

def load_and_merge(enrollment_csv, academics_csv, demos_csv, key):
    df_enroll = pd.read_csv(enrollment_csv)
    df_acad = pd.read_csv(academics_csv)
    df_demo = pd.read_csv(demos_csv)
    df = df_enroll.merge(df_acad, on=key, how="left").merge(df_demo, on=key, how="left")
    return df

def safe_to_datetime(series):
    return pd.to_datetime(series, errors="coerce")

def engineer_time_features(df, date_cols):
    if not date_cols:
        return df
    for col in date_cols:
        if col in df.columns:
            dt = safe_to_datetime(df[col])
            df[f"{col}_month"] = dt.dt.month
            df[f"{col}_year"] = dt.dt.year
            df[f"{col}_is_weekend"] = dt.dt.weekday >= 5
    # Example: lead time between application and enrollment
    if "application_date" in df.columns and "enrollment_date" in df.columns:
        app = safe_to_datetime(df["application_date"])
        enr = safe_to_datetime(df["enrollment_date"])
        df["application_to_enrollment_days"] = (enr - app).dt.days
    return df

def engineer_academic_trends(df):
    # Example GPA trend: current_gpa - hs_gpa
    if "current_gpa" in df.columns and "hs_gpa" in df.columns:
        df["gpa_delta"] = df["current_gpa"] - df["hs_gpa"]
    # Fail rate proxy
    if "courses_failed" in df.columns and "credits_completed" in df.columns:
        denom = df["credits_completed"].replace(0, np.nan)
        df["fail_rate"] = df["courses_failed"] / denom
        df["fail_rate"] = df["fail_rate"].fillna(0.0)
    return df

def select_features(df, categorical_cols, numeric_cols):
    cols = [c for c in categorical_cols + numeric_cols if c in df.columns]
    return df[cols].copy()

def drop_leaky_features(df, targets):
    # Remove columns that directly reveal the target or post-outcome info
    for t in targets:
        if t in df.columns:
            df = df.drop(columns=[t])
    return df