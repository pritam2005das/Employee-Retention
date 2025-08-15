# import necessary libraries
import streamlit as st
import pandas as pd
import cloudpickle

# load model
with open("model.pkl", "rb") as f:
    model = cloudpickle.load(f)

# Streamlit
st.title("Employee Retaintion")

# user input
satisfaction_level = st.number_input("satisfaction level", min_value= 0.0, max_value= 1.0, format= '%.2f')
last_evaluation = st.number_input("last evaluation", min_value= 0.0, max_value= 1.0, format= '%.2f')
number_project = st.number_input("number of project", min_value= 0)
average_monthly_hours = st.number_input("average monthly hours", min_value= 0)
time_spend_company = st.number_input("time spend company", min_value= 0, max_value= 10)
work_accident = st.selectbox("work accident", ['yes', 'no'])
promotion_last_5year = st.selectbox("promotion in last 5 year", ['yes', 'no'])
salary = st.selectbox("salary", ['low', 'medium', 'high'])

# prediction
if st.button("predict"):
    df = pd.DataFrame([{
        'satisfaction_level' : satisfaction_level,
        'last_evaluation' : last_evaluation,
        'number_project' : number_project,
        'average_montly_hours' : average_monthly_hours,
        'time_spend_company' : time_spend_company,
        'Work_accident' : 1 if work_accident == "yes" else 0,
        'promotion_last_5years' : 1 if promotion_last_5year == "yes" else 0,
        'salary' : salary
    }])
    prediction = model.predict(df)[0]
    probablity = model.predict_proba(df)[0][prediction]

    st.success(f"Prediction: {'Retain' if prediction == 0 else 'Left'}")

    st.write(f"Retain Probability: {probablity:.2%}")

