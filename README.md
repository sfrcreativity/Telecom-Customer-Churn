📱 Telecom Customer Churn & Customer Value Prediction
🚀 Dual-Model AI System (Regression + Classification)
<p align="center">
  <img src="https://i.imgur.com/kXDHj5Y.png" width="200"/>
</p>
🌟 Overview

This project predicts Customer Value and then uses that predicted value to compute Customer Churn Probability.
A complete real-time prediction system built using Machine Learning + Streamlit UI.

🔍 How It Works
1️⃣ Customer Value Prediction (Regression Model)

✔ Predicts how much a customer might be worth in monetary value
✔ Uses features like:

Call failures

SMS usage

Subscription length

Customer age

Payment amounts

Charge behaviors

👉 Output is automatically inserted into the churn model as an additional feature.

2️⃣ Churn Prediction (Classification Model)

✔ XGBoost-based model trained on processed telecom datasets
✔ Produces:

Churn Probability (%)

Churn or Not Churn (Binary Output)
✔ Helps identify risky customers early.

🧠 Why This Project Matters

🔹 Detect high-risk customers before they leave
🔹 Improve telecom customer retention
🔹 Understand spending + behavior patterns
🔹 Deployable as a real-time analytics dashboard

🛠 Technology Stack
Component	Technology
Backend ML	Python, Scikit-learn, XGBoost
Data Processing	Pandas, NumPy
Scaling	StandardScaler
App Interface	Streamlit
Model Storage	Pickle
Dataset	UCI Telecom Iranian Churn Dataset
📦 Installation
git clone https://github.com/sfrcreativity/Telecom-Customer-Churn.git
cd Telecom-Customer-Churn
pip install -r requirements.txt
streamlit run app.py

📁 Repository Structure
📦 Telecom-Customer-Churn
 ┣ 📂 models
 ┃ ┣ best_model.pkl
 ┃ ┣ linear_regression_model.pkl
 ┃ ┣ scaler.pkl
 ┃ ┗ scaler_regression.pkl
 ┣ 📂 images
 ┣ app.py
 ┣ requirements.txt
 ┗ README.md

📊 Features

✨ Modern Streamlit UI
✨ Two-step ML prediction pipeline
✨ Clean data preprocessing
✨ Scaling and model persistence
✨ Error-handling for missing/invalid features
✨ Developer-friendly modular code

📘 Dataset Citation
Citation: Iranian Churn [Dataset]. (2020).  
UCI Machine Learning Repository.  
https://doi.org/10.24432/C5JW3Z.

🤝 Contribution

Pull requests are welcome!
You may:

Improve UI

Add dark mode

Integrate database

Add charts & analytics

📬 Contact

📌 GitHub: https://github.com/sfrcreativity/Telecom-Customer-Churn

