
# 🧠 Medical Prediction Dashboard

A Streamlit web application that predicts **hospitalization status** (classification) and **severity score** (regression) of patients based on medical and demographic features using machine learning models trained with XGBoost and LightGBM.

---

## 📊 Features

- Upload an Excel file containing patient data
- Predict whether the patient is likely to be hospitalized
- Predict a severity score (Mild = 1 → Critical = 4)
- View predictions instantly on the dashboard
- Download the results as an Excel file
- Built using modern machine learning techniques

---

## 🔧 Technologies Used

| Component          | Library/Tool     | Purpose                                |
|--------------------|------------------|----------------------------------------|
| Web UI             | Streamlit        | Simple and interactive web app         |
| Data Processing    | Pandas, NumPy    | Handling and transforming input data   |
| ML Models          | XGBoost, LightGBM| Classification and Regression          |
| Model Persistence  | Joblib           | Saving/loading trained models          |
| File I/O           | openpyxl         | Excel file support                     |

---

## 📁 Folder Structure

```
medical_prediction_project/
├── app.py                         # Streamlit app
├── main.py                        # Model training script
├── data/
│   └── sample_prediction_input.xlsx
├── models/
│   ├── hospitalization_model.pkl  # XGBoost model
│   └── severity_model.pkl         # LightGBM model
├── output/
│   └── predictions_output.xlsx    # Output predictions
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 📥 Sample Input Format

Your Excel file should have the following columns:

| Patient_ID | Preexisting_Conditions | Date       | Symptoms                         |
|------------|------------------------|------------|----------------------------------|
| P1000      | Heart Disease          | 2024-07-23 | Cough                            |
| P1001      | Asthma                 | 2024-12-31 | Fever, Headache                  |
| P1002      | Asthma                 | 2024-07-10 | Cough, Shortness of breath       |
| ...        | ...                    | ...        | ...                              |

⚠️ Do **not** include the `Hospitalized` or `Severity` column. The app will predict these.

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/medical-prediction-dashboard.git
   cd medical_prediction_dashboard
   ```

2. **Create virtual environment (optional)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🌍 Deploy on Streamlit Cloud (Free)

1. Push this project to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App** → Connect your repo
4. Select `app.py` as the entry point
5. Click **Deploy** ✅

---

## ✅ Example Prediction Output

| Patient_ID | Predicted_Hospitalized | Predicted_Severity_Score |
|------------|------------------------|---------------------------|
| P1000      | No                     | 1                         |
| P1001      | Yes                    | 3                         |

---

## 📌 Future Improvements

- Add user authentication
- Collect feedback and corrections from doctors
- Add visual analytics (charts, heatmaps, etc.)
- Connect directly with Power BI or dashboards
- Train with larger real-world datasets

---

## 👨‍⚕️ Author

**Mukul Chaudhary**  
Medical Data Science Project  
Built with ❤️ using Streamlit and Python

🔗 [LinkedIn](https://www.linkedin.com/in/mukul-613866201/)  
🌐 [Portfolio](https://mukul20csu355.github.io/portfolio/)  
Medical Data Science Project  
Built with ❤️ using Streamlit and Python
