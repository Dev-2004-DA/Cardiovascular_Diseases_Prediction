# Cardiovascular Disease Risk Predictor

**Live Demo → [cardiovasculardiseasesprediction-equ3p2xhkmg65ejh7tesis.streamlit.app](https://cardiovasculardiseasesprediction-equ3p2xhkmg65ejh7tesis.streamlit.app)**

A machine learning web app that predicts cardiovascular disease risk from patient vitals. Built on 70,000 medical records using Random Forest classification, deployed as an interactive Streamlit application.

---

## Results

| Metric | Value |
|--------|-------|
| Cross-validated Accuracy | ~76% |
| OOB Score | ~73% |
| Disease Recall (after tuning) | 85% |
| Baseline Recall | 69% |
| Classifiers Benchmarked | 10+ |

---

## What the app does

Enter patient details — age, blood pressure, cholesterol, BMI, lifestyle factors — and the model returns:
- Risk probability (0–100%)
- Colour-coded verdict (Low / Moderate / High)
- Visual risk gauge
- Top feature importance breakdown

---

## Key decisions made

**Why Random Forest over other models?**
After benchmarking 10+ classifiers including Logistic Regression, Gradient Boosting, XGBoost, and SVM, Random Forest achieved the best balance of accuracy (~76% CV) and stability (OOB ~73%) with no severe overfitting.

**Why threshold tuning?**
Default 0.5 threshold gave 69% recall — too many missed disease cases for a screening tool. Tuning the ROC-AUC threshold to prioritise sensitivity raised recall to 85%, accepting a small precision trade-off. In a medical screening context, false negatives are more costly than false positives.

**Most important features**
Systolic and diastolic blood pressure together account for ~70% of feature importance — consistent with clinical literature on cardiovascular risk.

---

## Tech stack

| Layer | Tool |
|-------|------|
| ML | Scikit-learn (Random Forest) |
| Data | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| App | Streamlit |
| Model serialisation | Joblib |
| Deployment | Streamlit Community Cloud |
| Language | Python 3.12 |

---

## Project structure

```
├── application.py       # Streamlit app
├── rf_model.pkl         # Trained Random Forest model
├── requirements.txt     # Dependencies
├── runtime.txt          # Python 3.12 pin for deployment
└── README.md
```

---

## Run locally

```bash
git clone https://github.com/Dev-2004-DA/Cardiovascular_Diseases_Prediction
cd Cardiovascular_Diseases_Prediction
pip install -r requirements.txt
streamlit run application.py
```

---

## Dataset

- Source: Kaggle — Cardiovascular Disease Dataset
- 70,000 patient records
- 11 features: age, gender, height, weight, systolic BP, diastolic BP, cholesterol, glucose, smoking, alcohol, physical activity
- Binary target: presence or absence of cardiovascular disease

---

## Disclaimer

This tool is for educational purposes only and does not constitute medical advice.
