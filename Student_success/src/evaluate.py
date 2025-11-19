import numpy as np
from sklearn.metrics import (
    roc_auc_score, average_precision_score,
    f1_score, precision_score, recall_score,
    mean_absolute_error, r2_score
)

def evaluate_classifier(model, X_val, y_val):
    prob = model.predict_proba(X_val)[:, 1]
    pred = (prob >= 0.5).astype(int)
    metrics = {
        "roc_auc": roc_auc_score(y_val, prob),
        "pr_auc": average_precision_score(y_val, prob),
        "f1": f1_score(y_val, pred),
        "precision": precision_score(y_val, pred),
        "recall": recall_score(y_val, pred)
    }
    return metrics

def evaluate_regressor(model, X_val, y_val):
    pred = model.predict(X_val)
    metrics = {
        "mae": float(np.mean(np.abs(pred - y_val))),
        "r2": r2_score(y_val, pred)
    }
    return metrics