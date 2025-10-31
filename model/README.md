# Boston Housing Price Prediction

This project demonstrates how to build and use a linear regression model to predict housing prices using the Boston Housing dataset. It simulates a real-world scenario where socioeconomic and environmental factors influence outcomes—similar to how accident severity might be predicted in traffic safety studies.

---

## Dataset

The dataset includes 13 features and one target variable:

- **Target (Dependent Variable):**
  - `MEDV`: Median value of owner-occupied homes in $1000s

- **Features (Independent Variables):**
  - `CRIM`: Crime rate per capita
  - `ZN`: Proportion of residential land zoned
  - `INDUS`: Proportion of non-retail business acres
  - `CHAS`: Charles River dummy variable (1 if tract bounds river)
  - `NOX`: Nitric oxide concentration
  - `RM`: Average number of rooms per dwelling
  - `AGE`: Proportion of owner-occupied units built before 1940
  - `DIS`: Distance to employment centers
  - `RAD`: Index of accessibility to radial highways
  - `TAX`: Property tax rate
  - `PTRATIO`: Pupil-teacher ratio
  - `B`: Proportion of Black population
  - `LSTAT`: % lower status population

---

## Model Overview

- **Algorithm:** Linear Regression
- **Library:** scikit-learn
- **Training/Test Split:** 80/20
- **Performance Metric:** R² score

---

## How to Run

1. Install dependencies:

   pip install pandas scikit-learn joblib

   - Run the script:

python boston_price_model.py

- Output includes:
- Model training R² score
- Saved model file: boston_price_model.pkl
- Predicted price for a sample input

 Sample PredictionThe script includes a hypothetical input like:{
  'CRIM': 0.05,
  'ZN': 20.0,
  'INDUS': 5.0,
  'CHAS': 0,
  'NOX': 0.45,
  'RM': 6.5,
  'AGE': 60.0,
  'DIS': 4.0,
  'RAD': 4,
  'TAX': 300.0,
  'PTRATIO': 18.0,
  'B': 390.0,
  'LSTAT': 10.0
}

The model predicts the corresponding house price in thousands of dollars. Broader ImpactThis project mirrors how predictive models can be used in underdeveloped countries to:- Identify high-risk areas for urban planning
- Allocate resources for housing or traffic safety
- Support data-driven policy decisions

📸 ScreenshotsInclude screenshots of:- Dataset preview

![alt text](image.png) 

👤 AuthorDenis — Backend Developer & Data Science Enthusiast
📍 Kiambu, Kenya