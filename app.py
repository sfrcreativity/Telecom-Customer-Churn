import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load model, scaler, and columns
# -----------------------------
with open("linear_regression_model.pkl", "rb") as f:
    model1 = pickle.load(f)
with open("scaler_regression.pkl", "rb") as f:
    scaler1 = pickle.load(f)
with open("model_columns_regression.pkl", "rb") as f:
    model_columns_regression = pickle.load(f)
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

# Beautiful Header
st.markdown("""
    <style>
        .main-header {
            padding: 20px;
            border-radius: 12px;
            background: rgba(0, 122, 204, 0.15);
            backdrop-filter: blur(6px);
            border: 1px solid rgba(255,255,255,0.2);
            text-align: center;
            margin-bottom: 20px;
        }
        .main-header h1 {
            color: #FFF;
            font-weight: 700;
            font-size: 36px;
        }
        .main-header p {
            font-size: 16px;
            color: #DDD;
        }
    </style>

    <div class="main-header">
        <h1>📡 Telecom Customer Churn Prediction</h1>
        <p>AI-powered prediction system using Linear Regression + XGBoost</p>
    </div>
""", unsafe_allow_html=True)


st.markdown(
    """
    A machine learning–powered app that predicts telecom customer churn based on customer behavior, usage statistics, subscription details, and complaints. It uses Linear Regression for customer value estimation and XGBoost for churn prediction.
    """
)
st.markdown("---")
st.write("Adjust the features and get real-time churn prediction.")

subscription_options = {
    "3 months": 3,
    "6 months": 6,
    "12 months": 12,
    "24 months": 24,
    "36 months": 36
}

status_options = {
    "Active": 1,
    "Not Active": 2
}

tariff_plan_options = {
    "Pay as you go": 1,
    "Contractual": 2
}

complains_options = {
    "No Complaint": 0,
    "Complaint": 1
}


charge_amount_options = {
    "Free":0,
    "Minimal": 1,
    "Very Low": 2,
    "Low": 3,
    "Medium-Low": 4,
    "Medium": 5,
    "Medium-High": 6,
    "High": 7,
    "Very High": 8,
    "Premium-Low": 9,
    "Premium-High": 10
}

complains = st.selectbox("Complains", list(complains_options.keys()))
subscription = st.selectbox("Subscription  Length", list(subscription_options.keys()))
tariff_plan = st.selectbox("Tariff Plan", list(tariff_plan_options.keys()))
status = st.selectbox("Status", list(status_options.keys()))
charge_amount = st.selectbox("Charge Amount", list(charge_amount_options.keys()))
# -----------------------------
# User input function
# -----------------------------
def user_input():
    data = {
    # Checkbox for Complains (binary)
    "Complains": [(complains_options[complains])],
    "Subscription  Length": [(subscription_options[subscription])],
    # Friendly select boxes mapped to numeric values directly
    "Tariff Plan": [(tariff_plan_options[tariff_plan])],
    "Status": [(status_options[status])],

    # Numeric sliders
    "Call  Failure": [st.slider("Call Failure", 0, 36, 6)],
    "Charge  Amount": [(charge_amount_options[charge_amount])],
    "Seconds of Use": [st.slider("Seconds of Use", 0, (subscription_options[subscription]*60)*60, 3000)],
    "Frequency of use": [st.slider("Frequency of Use", 0, 255, 70)],
    "Frequency of SMS": [st.slider("Frequency of SMS", 0, 522, 73)],
    "Distinct Called Numbers": [st.slider("Distinct Called Numbers", 0, 97, 24)],
    
    # Capture age and use it for Age Group
    "Age": [age := st.slider("Age", 15, 55, 31)],

    # Age Group computed inline based on age
    "Age Group": [
        1 if 15 <= age <= 20 else
        2 if 21 <= age <= 30 else
        3 if 31 <= age <= 40 else
        4 if 41 <= age <= 50 else
        5
    ]}
    return pd.DataFrame(data)

input_df = user_input()
input_reg_df = input_df.copy()

# -----------------------------
# Align input columns to model
# -----------------------------
# Add missing columns
input_reg_df = input_df.drop(["Status","Charge  Amount","Call  Failure"], axis=1,errors='ignore')

for col in model_columns_regression:
    if col not in input_reg_df.columns:
        input_reg_df[col] = 0

# Reorder columns for regression
input_reg_df = input_reg_df[model_columns_regression]



# -----------------------------
# Predict
# -----------------------------
if st.button("Predict Customer Churn"):
    # Predict Customer Value
    try:
        X1_scaled = scaler1.transform(input_reg_df)
        pred1 = model1.predict(X1_scaled)
    except Exception as e:
        st.error(f"Error: {e}")    

    # Add missing columns
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_churn_df = input_df[model_columns]
    input_churn_df["Customer Value"] = pred1


    try:
        X_scaled = scaler.transform(input_churn_df)
        pred = model.predict(X_scaled)
        prob = model.predict_proba(X_scaled)[:,1]
        st.subheader("Prediction Result")
        if pred[0]==1:
            st.error("Customer may leave soon ⚠️")
        else:
            st.success("Retained Customer ✅")
        st.write(f"Probability of leaving: {prob[0]*100:.2f}%")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.markdown("""
    <div class="footer">
        Made with ❤️ using Streamlit  
        | <a href="https://github.com/sfrcreativity/Telecom-Customer-Churn" target="_blank">GitHub Project</a>  
            <br>
        Dataset: Iranian Churn [<a href="https://doi.org/10.24432/C5JW3Z" target="_blank">Dataset </a>]. (2020).
            <br> UCI Machine Learning Repository.
    </div>
""", unsafe_allow_html=True)