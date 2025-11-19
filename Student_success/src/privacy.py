import pandas as pd

PII_COLS_DEFAULT = ["student_name", "email", "phone", "national_id"]

def remove_pii(df, pii_cols=PII_COLS_DEFAULT):
    present = [c for c in pii_cols if c in df.columns]
    return df.drop(columns=present)

def hash_ids(df, id_col="student_id", salt="static_salt_change_me"):
    if id_col in df.columns:
        df[id_col] = (df[id_col].astype(str) + salt).apply(lambda x: hash(x))
    return df

def clip_sensitive_numeric(df, cols, min_val=None, max_val=None):
    for c in cols:
        if c in df.columns:
            if min_val is not None:
                df[c] = df[c].clip(lower=min_val)
            if max_val is not None:
                df[c] = df[c].clip(upper=max_val)
    return df