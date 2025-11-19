import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

from config import (
    ENROLLMENT_CSV, ACADEMICS_CSV, DEMOS_CSV, PRIMARY_KEY,
    TARGET_ENROLL, TARGET_SUPPORT, SUPPORT_AS_REGRESSION,
    CATEGORICAL_COLS, NUMERIC_COLS, DATE_COLS,
    RANDOM_STATE, TEST_SIZE
)
from src.features import (
    load_and_merge, engineer_time_features, engineer_academic_trends,
    select_features, drop_leaky_features
)
from src.privacy import remove_pii, hash_ids
from src.models import build_preprocessor, build_enrollment_model, build_support_model
from src.evaluate import evaluate_classifier, evaluate_regressor

def prepare_dataset():
    df = load_and_merge(ENROLLMENT_CSV, ACADEMICS_CSV, DEMOS_CSV, PRIMARY_KEY)
    # Privacy hygiene
    df = remove_pii(df)
    df = hash_ids(df, id_col=PRIMARY_KEY)

    # Feature engineering
    df = engineer_time_features(df, DATE_COLS)
    df = engineer_academic_trends(df)

    # Split out targets
    y_enroll = df[TARGET_ENROLL].astype(int)
    y_support = df[TARGET_SUPPORT] if TARGET_SUPPORT in df.columns else None
    if y_support is not None and not SUPPORT_AS_REGRESSION:
        y_support = y_support.astype(int)

    # Build feature matrix
    X = select_features(df, CATEGORICAL_COLS, NUMERIC_COLS)
    X = drop_leaky_features(X, [TARGET_ENROLL, TARGET_SUPPORT])

    return X, y_enroll, y_support

def train_enrollment(X, y):
    pre = build_preprocessor(
        [c for c in X.columns if c in CATEGORICAL_COLS],
        [c for c in X.columns if c in NUMERIC_COLS]
    )
    model = build_enrollment_model(pre, random_state=RANDOM_STATE)
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    model.fit(X_train, y_train)
    metrics = evaluate_classifier(model, X_val, y_val)
    return model, metrics

def train_support(X, y):
    pre = build_preprocessor(
        [c for c in X.columns if c in CATEGORICAL_COLS],
        [c for c in X.columns if c in NUMERIC_COLS]
    )
    model = build_support_model(pre, regression=SUPPORT_AS_REGRESSION, random_state=RANDOM_STATE)
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE,
        stratify=y if not SUPPORT_AS_REGRESSION else None
    )
    model.fit(X_train, y_train)
    if SUPPORT_AS_REGRESSION:
        metrics = evaluate_regressor(model, X_val, y_val)
    else:
        metrics = evaluate_classifier(model, X_val, y_val)
    return model, metrics

def persist(model, path):
    joblib.dump(model, path)

def run_training():
    X, y_enroll, y_support = prepare_dataset()

    enroll_model, enroll_metrics = train_enrollment(X, y_enroll)
    print("Enrollment metrics:", json.dumps(enroll_metrics, indent=2))

    persist(enroll_model, "student_success/enrollment_model.joblib")

    if y_support is not None:
        support_model, support_metrics = train_support(X, y_support)
        print("Support metrics:", json.dumps(support_metrics, indent=2))
        persist(support_model, "student_success/support_model.joblib")

if __name__ == "__main__":
    run_training()