import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, mean_squared_error
import xgboost as xgb
import lightgbm as lgb
import joblib
import os

# Load data
df = pd.read_excel('data/patient_data.xlsx')

# Preprocessing
df.drop(columns=['Patient_ID'], inplace=True, errors='ignore')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Severity_Score'] = df['Severity'].map({'Mild': 1, 'Moderate': 2, 'Severe': 3, 'Critical': 4})
df['Hospitalized'] = df['Hospitalized'].map({'Yes': 1, 'No': 0})
df.ffill(inplace=True)

if 'Date' in df.columns:
    df.drop(columns=['Date'], inplace=True)

# One-hot encode
cat_cols = df.select_dtypes(include='object').columns
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
df.columns = df.columns.str.replace(r'[\"\\/:*?<>|,]', '_', regex=True)  # clean names

# Classification target
X_cls = df.drop(columns=['Hospitalized', 'Severity_Score'])
y_cls = df['Hospitalized']

X_train, X_test, y_train, y_test = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)

model_cls = xgb.XGBClassifier()
model_cls.fit(X_train, y_train)

print("Classification Report:\n", classification_report(y_test, model_cls.predict(X_test)))

# Regression target
X_reg = df.drop(columns=['Hospitalized', 'Severity_Score'])
y_reg = df['Severity_Score']

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

model_reg = lgb.LGBMRegressor()
model_reg.fit(X_train_r, y_train_r)

print("MSE (Regression):", mean_squared_error(y_test_r, model_reg.predict(X_test_r)))

# Save models and columns
os.makedirs('models', exist_ok=True)
joblib.dump(model_cls, 'models/hospitalization_model.pkl')
joblib.dump(model_reg, 'models/severity_model.pkl')
joblib.dump(X_cls.columns.tolist(), 'models/training_columns.pkl')  # ✅ Add this once
