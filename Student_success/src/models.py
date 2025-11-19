from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

def build_preprocessor(categorical_cols, numeric_cols):
    cat_pipe = Pipeline(steps=[
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    num_pipe = Pipeline(steps=[
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler(with_mean=False))
    ])
    pre = ColumnTransformer(
        transformers=[
            ("cat", cat_pipe, categorical_cols),
            ("num", num_pipe, numeric_cols),
        ],
        remainder="drop",
        n_jobs=None
    )
    return pre

def build_enrollment_model(preprocessor, random_state=42):
    clf = Pipeline(steps=[
        ("pre", preprocessor),
        ("model", RandomForestClassifier(
            n_estimators=300,
            max_depth=None,
            n_jobs=-1,
            random_state=random_state,
            class_weight="balanced"
        ))
    ])
    return clf

def build_support_model(preprocessor, regression=False, random_state=42):
    if regression:
        model = RandomForestRegressor(
            n_estimators=300, max_depth=None, n_jobs=-1, random_state=random_state
        )
    else:
        model = RandomForestClassifier(
            n_estimators=300, max_depth=None, n_jobs=-1, random_state=random_state, class_weight="balanced"
        )
    pipe = Pipeline(steps=[
        ("pre", preprocessor),
        ("model", model)
    ])
    return pipe