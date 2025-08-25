# 🏢 Employee Retention Prediction

This project predicts whether an employee will **stay** or **leave the organization** based on various factors such as satisfaction level, last evaluation, number of projects, working hours, salary, and promotion history. It is built using **Machine Learning models** and deployed with a **Streamlit web app** for interactive predictions.  

---

## 📌 Objective
The primary objective of this project is to:
- Analyze employee data and identify the key factors influencing employee retention.
- Build a predictive machine learning model to classify employees as "Retain" or "Left".
- Deploy an interactive web app to make predictions for HR decision-making.

---

## 📊 Dataset
- **Source:** HR Analytics Employee Attrition Dataset  
- **Features:**  
  - `satisfaction_level`  
  - `last_evaluation`  
  - `number_project`  
  - `average_monthly_hours`  
  - `time_spend_company`  
  - `work_accident`  
  - `promotion_last_5years`  
  - `salary`  

- **Target Variable:**  
  - `left` (1 = Retain, 0 = Left)

---

## 🛠️ Technologies Used
- **Python**
- **Pandas, NumPy** → Data preprocessing
- **Matplotlib, Seaborn** → Exploratory Data Analysis (EDA)
- **Scikit-learn** → Model training & evaluation
- **Streamlit** → Web application deployment
- **Cloudpickle** → Model serialization

---

## 🔄 Methodology
1. **Data Collection & Preprocessing**  
   - Imported HR dataset, handled missing values, and encoded categorical variables.  

2. **Exploratory Data Analysis (EDA)**  
   - Visualized distributions, correlations, and feature importance.  
   - Identified key patterns (e.g., low satisfaction and high working hours → higher attrition).  

3. **Model Training & Evaluation**  
   - Built classification models (Logistic Regression, Random Forest, Gradient Boosting, etc.).  
   - Evaluated using accuracy, precision, recall, and F1-score.  
   - Selected the best-performing model and saved it as `model.pkl`.  

4. **Deployment**  
   - Streamlit app developed (`app.py`) with user-friendly input forms.  
   - Loads `model.pkl` and predicts employee retention status in real-time.  

---

## 📈 Findings
- Employees with **low satisfaction level** and **long working hours** are more likely to leave.  
- **Salary** and **promotion history** play significant roles in retention.  
- Model successfully predicts employee attrition with high accuracy (≈ 98%).

---

## 🚀 Streamlit App Deployment
The app provides a simple HR-friendly interface:  
1. Enter employee details (satisfaction level, projects, hours, etc.).  
2. Click **Predict** to see whether the employee will **Retain** or **Leave**, along with probability.  

📌 Example Screenshot:  
*(Insert Streamlit app screenshot here)*  

---

## 📂 Project Structure

**Employee-Retention/**
  - `app.py`
  - `data_processing.ipynb`
  - `hr_employee_churn_data.csv`
  - `hr_employee_churn_data_cleaned.csv`
  - `model.ipynb`
  - `model.pkl`
  - `requirements.txt`
  - `README.md`
  - `.devcontainer/`
  - `catboost_info/`
  - `Employee Retention Dashboard.pbix`
  - `Employee Retention Predictor.pptx`

---

## ✅ Conclusion
This project demonstrates how **machine learning can effectively predict employee attrition** and assist HR teams in making data-driven decisions. By analyzing satisfaction, workload, salary, and promotions, organizations can **proactively identify at-risk employees** and implement retention strategies.  

- 🔗 **Project link:** [Employee-Retention](https://github.com/pritam2005das/Employee-Retention)  
- 🌐 **Try it live:** [Employee-Retention](https://employee-retaintion-wu7ngshzq4dp88ntc8i878.streamlit.app/)

---

## 🔮 Future Scope
- Deploy as a **full-stack HR Analytics Dashboard** with visual insights.  
- Integrate with **real-time employee databases** for live monitoring.  
- Extend model with **deep learning techniques** for higher accuracy.  
- Add **explainability (SHAP, LIME)** to show why an employee is predicted to leave.  

---

## 👨‍💻 Author
- **Pritam Das**  
- GitHub: [pritam2005das](https://github.com/pritam2005das)
