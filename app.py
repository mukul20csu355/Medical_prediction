import streamlit as st
import pandas as pd
import joblib
import os

# Load trained models
model_cls = joblib.load('models/hospitalization_model.pkl')
model_reg = joblib.load('models/severity_model.pkl')
model_columns = joblib.load('models/training_columns.pkl')

# UI layout
st.set_page_config(page_title="Medical Prediction App", layout="wide")
st.title("🏥 Medical Prediction Dashboard")
st.markdown("Upload an Excel file to predict **Hospitalization** and **Severity Score**.")

# Upload file
uploaded_file = st.file_uploader("📤 Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("📄 Uploaded Data Preview:")
    st.dataframe(df.head())

    # Drop target columns if accidentally included
    df.drop(columns=['Severity', 'Hospitalized'], errors='ignore', inplace=True)

    # Save Patient_IDs for output
    patient_ids = df['Patient_ID'] if 'Patient_ID' in df.columns else [f"P{i+1000}" for i in range(len(df))]

    # Preprocessing
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.ffill(inplace=True)
    df.drop(columns=['Patient_ID'], errors='ignore', inplace=True)
    df.drop(columns=['Date'], errors='ignore', inplace=True)

    # One-hot encode input
    df_encoded = pd.get_dummies(df)
    for col in model_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[model_columns]

    # Predictions
    pred_cls = model_cls.predict(df_encoded)
    pred_reg = model_reg.predict(df_encoded)

    # Format predictions
    pred_cls_labels = ['Yes' if val == 1 else 'No' for val in pred_cls]
    pred_reg_labels = [round(score) for score in pred_reg]

    results_df = pd.DataFrame({
        'Patient_ID': patient_ids,
        'Predicted_Hospitalized': pred_cls_labels,
        'Predicted_Severity_Score': pred_reg_labels
    })

    st.subheader("📊 Prediction Results")
    st.dataframe(results_df)

    # Save predictions
    os.makedirs('output', exist_ok=True)
    output_path = 'output/predictions_output.xlsx'
    results_df.to_excel(output_path, index=False)
    st.success(f"✅ Predictions saved to `{output_path}`")

    # Download button
    with open(output_path, 'rb') as f:
        st.download_button("📥 Download Predictions Excel", f, file_name="predictions_output.xlsx")
