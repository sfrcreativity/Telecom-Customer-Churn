
<p align="center">
  <img src="https://i.imgur.com/kXDHj5Y.png" width="160"/>
</p>

<h1 align="center">📡 Telecom Customer Churn & Value Prediction</h1>

<p align="center">
  A Machine Learning project that predicts <b>customer value</b> and <b>churn probability</b> using Regression + XGBoost Classification models.
</p>

---

## 🚀 **Project Overview**

This project performs **two-step prediction** to generate deeper insights for telecom companies:

### 🔹 **1️⃣ Customer Value Prediction (Regression Model)**
- Predicts customer monetary value  
- Uses call failures, SMS usage, subscription length, age, and more  
- Output is auto-fed into the churn model

### 🔹 **2️⃣ Churn Prediction (XGBoost Classification Model)**
- Predicts churn probability (%)  
- Uses cleaned + scaled telecom data  
- Helps companies identify high-risk customers early

---

## 🔥 **Features**
- Interactive **Streamlit Web App**
- Dual-model prediction (Regression + Classification)
- Customer value auto-injection into churn model
- Advanced preprocessing and feature scaling
- Visualization-friendly structure
- Production-ready model saving using Pickle

---

## 🧠 **Technology Stack**
| Layer | Tools |
|-------|-------|
| Programming | Python 3 |
| ML | Scikit-learn, XGBoost |
| Data | Pandas, NumPy |
| Deployment | Streamlit |
| Model Storage | Pickle |
| Dataset | UCI – Iranian Telecom Churn |

---

## 📦 **Dataset Source**
Citation: Iranian Churn [Dataset]. (2020). UCI Machine Learning Repository.  
https://doi.org/10.24432/C5JW3Z

---

## 📂 **Project Structure**
```
Telecom-Customer-Churn/
│── app.py
│── linear_regression_model.pkl
│── best_model.pkl
│── scaler.pkl
│── scaler_regression.pkl
│── model_columns.pkl
│── model_columns_regression.pkl
│── requirements.txt
│── README.md
└── assets/
      └── telecom.png  (optional logo)
```

---

## 🛠️ **Installation & Setup**

### 🔧 **1. Clone the repository**
```bash
git clone https://github.com/sfrcreativity/Telecom-Customer-Churn.git
```

### 📁 **2. Navigate to project**
```bash
cd Telecom-Customer-Churn
```

### 📦 **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### ▶️ **4. Run the Streamlit App**
```bash
streamlit run app.py
```

---

## 🌐 **Live App (Optional Deployment)**  
If you deploy on Streamlit Cloud or HuggingFace later, add link here.

---

## 🧮 **Model Performance**

### 📈 Regression
- **R² = 0.98**
- **MAE = 38.99**
- **RMSE = 72.66**

### 📊 Classification (XGBoost)
- High accuracy with optimized feature scaling  
- Predicts churn probability + binary output

---

## 📥 **Download Project (ZIP)**
👉 **Direct Download:**  
https://github.com/sfrcreativity/Telecom-Customer-Churn/archive/refs/heads/main.zip

---

## 🤝 **Contributing**
Pull requests are welcome! For major changes, open an issue first to discuss.

---

## 📧 **Author**
**GitHub:** https://github.com/sfrcreativity/Telecom-Customer-Churn  

---

## ⭐ **Support**
If you like this project, please ⭐ the repo — it helps a lot!
