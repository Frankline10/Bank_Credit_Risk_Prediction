import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="Bank Credit Risk Prediction",
    page_icon="🏦",
    layout="centered"
)

# Title
st.title("🏦 Bank Credit Risk Prediction")
st.markdown("Predict whether a customer is a **Credit Risk** or **Not a Credit Risk**.")

# Loading Pipeline
pipeline = joblib.load(
    "/Users/soujanyaprokashsingha/Documents/Data Analyst_Science/Professional Projects/Datamites Projects/Bank_Credit_Risk_Prediction/models/credit_risk_pipeline.pkl"
)

# Sidebar
st.sidebar.header("Customer Information")

# User Inputs
total_accounts = st.sidebar.number_input(
    "Total Accounts",
    min_value=0,
    value=5
)

total_credit_limit = st.sidebar.number_input(
    "Total Credit Limit",
    min_value=0.0,
    value=50000.0
)

total_current_balance = st.sidebar.number_input(
    "Total Current Balance",
    min_value=0.0,
    value=20000.0
)

credit_utilization_ratio = st.sidebar.number_input(
    "Credit Utilization Ratio",
    min_value=0.0,
    max_value=1.0,
    value=0.30
)

total_past_due = st.sidebar.number_input(
    "Total Past Due",
    min_value=0.0,
    value=0.0
)

total_enquiries = st.sidebar.number_input(
    "Total Enquiries",
    min_value=0,
    value=2
)

avg_account_age_days = st.sidebar.number_input(
    "Average Account Age (Days)",
    min_value=0,
    value=365
)

avg_payment_amount = st.sidebar.number_input(
    "Average Payment Amount",
    min_value=0.0,
    value=5000.0
)

# Creating Input DataFrame
input_data = pd.DataFrame({
    "total_accounts": [total_accounts],
    "total_credit_limit": [total_credit_limit],
    "total_current_balance": [total_current_balance],
    "credit_utilization_ratio": [credit_utilization_ratio],
    "total_past_due": [total_past_due],
    "total_enquiries": [total_enquiries],
    "avg_account_age_days": [avg_account_age_days],
    "avg_payment_amount": [avg_payment_amount]
})

# Display Input
st.subheader("📋 Customer Input Data")
st.dataframe(input_data)

# Prediction Button
if st.button("Predict Credit Risk"):

    # Prediction
    prediction = pipeline.predict(input_data)[0]

    # Probability
    probability = pipeline.predict_proba(input_data)[0][1]

    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to be a Credit Risk")
    else:
        st.success("✅ Customer is Not a Credit Risk")

    st.subheader("📈 Risk Probability")

    st.progress(float(probability))

    st.write(f"Risk Probability: **{probability:.2%}**")