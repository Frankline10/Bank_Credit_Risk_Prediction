# 🏦 Bank Credit Risk Prediction System

A Machine Learning based Credit Risk Prediction System developed to identify potential risky customers by analyzing financial behavior, credit utilization patterns, account history, and enquiry activities.

This project demonstrates an end-to-end Data Science workflow including:
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Selection
- Model Building
- Model Evaluation
- Risk Ranking using Gini & ROC-AUC
- Deployment Preparation

---

# 📌 Project Objective

The main objective of this project is to build a predictive system capable of classifying customers into:
- Low Risk Customers
- High Risk Customers

This helps financial institutions:
- Reduce loan default risk
- Improve lending decisions
- Automate customer risk assessment
- Enhance portfolio management

---

# ❓ Problem Statement

Banks and financial institutions face significant losses due to loan defaults and poor credit risk assessment.

Traditional rule-based systems are often insufficient for handling large-scale customer behavioral data.

This project uses Machine Learning techniques to:
- Analyze customer financial behavior
- Detect risky repayment patterns
- Predict probability of default
- Improve risk ranking capability

---

# 📂 Dataset Overview

The project uses banking and customer credit-related datasets containing:
- Customer account details
- Credit limits
- Current balances
- Enquiry history
- Repayment behavior
- Delinquency information

The data was merged and transformed into a customer-level analytical dataset for modeling.

---

# 📊 Exploratory Data Analysis (EDA)

Several important insights were identified during EDA:

- Customers with high credit utilization showed higher default probability
- Recent credit enquiries were strong indicators of financial stress
- Delinquency-related behavior significantly impacted risk prediction
- Financial variables contained skewed distributions and outliers
- Target variable was imbalanced, requiring robust evaluation metrics

EDA helped guide:
- Feature engineering strategy
- Model selection
- Risk ranking approach

---

# ⚙️ Feature Engineering

Domain-specific engineered features were created to improve predictive performance.

## Major Engineered Features

| Feature | Description |
|---|---|
| credit_utilization_ratio | Used credit compared to total credit limit |
| avg_credit_limit | Average credit limit per account |
| avg_current_balance | Average outstanding balance |
| count_enquiry_90 | Enquiries in last 90 days |
| count_enquiry_365 | Enquiries in last 365 days |
| total_accounts | Total active accounts |
| delinquency_features | Repayment irregularity indicators |

Feature engineering significantly improved the model’s discriminatory power.

---

# 🤖 Machine Learning Models Used

The following models were trained and evaluated:

| Model | Purpose |
|---|---|
| Logistic Regression | Baseline Model |
| Random Forest | Ensemble Learning |
| XGBoost | Final Selected Model |

---

# 📈 Model Evaluation

The models were evaluated using:
- ROC-AUC Score
- Gini Score
- Precision
- Recall
- F1 Score
- Confusion Matrix

## Gini Formula

```math
Gini = 2 × ROC-AUC - 1
```

## Final Model Performance

| Metric | Value |
|---|---|
| ROC-AUC Score | ~0.77 |
| Gini Score | ~0.54 |

The XGBoost model achieved the best overall performance and rank ordering capability.

---

# 📌 Rank Ordering Capability

The final model successfully ranked customers based on risk probability.

The model:
- Assigned higher probabilities to risky customers
- Distinguished good customers from bad customers effectively
- Improved portfolio-level risk segmentation

This makes the model suitable for credit approval and risk assessment use cases.

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Joblib

## Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

# 🔄 Project Workflow

```text
Data Collection
       ↓
Data Cleaning & Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Feature Selection
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Selection
       ↓
Deployment Preparation
```

---

# 🚧 Challenges Faced

Some major challenges encountered during the project included:

- Creating meaningful business-driven features
- Selecting the most relevant predictive variables
- Handling highly skewed financial data
- Managing feature correlations
- Preventing overfitting
- Handling imbalanced target classes
- Maintaining feature consistency during deployment preparation

Additional deployment-related issues were faced while attempting to build a real-time web application.

---

# 🚀 Future Improvements

Future enhancements planned for the project include:

- Building a fully functional Streamlit/Flask web application
- Real-time prediction system
- Cloud deployment
- Explainable AI integration (SHAP values)
- Advanced hyperparameter tuning
- Automated monitoring and model drift detection

---

# 📁 Repository Structure

```text
Bank-Credit-Risk-Prediction/
│
├── data/
├── notebooks/
├── models/
├── app/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚡ Installation & Setup

## Clone the Repository

```bash
git clone https://github.com/Frankline10/Bank_Credit_Risk_Prediction.git
```

## Navigate to Project Folder

```bash
cd Bank_Credit_Risk_Prediction
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Jupyter Notebook

```bash
jupyter notebook
```

---

# 👨‍💻 Author

## Soujanya Prokash Singha

B.Tech – Computer Science & Engineering  
Aspiring Data Analyst & Data Scientist

### Skills
- Python
- SQL
- Machine Learning
- Power BI
- Statistics
- Data Analysis

---

# 📌 Conclusion

This project demonstrates how Machine Learning can be effectively applied to real-world banking and financial risk assessment problems.

By combining:
- Exploratory Data Analysis
- Feature Engineering
- Predictive Modeling
- Risk Ranking

the system successfully identifies risky customers and supports better financial decision-making.
