# Project Title
# ╔════════════════════════════════════════════════════╗
# ║ 📉 Customer Churn Prediction - Business Analytics  ║
# ║ 📊 Machine Learning in Python                      ║
# ║ 🛠️  By: Nishkarsh Pandey (Nish2005karsh)                   ║
# ╚════════════════════════════════════════════════════╝


## 👤 Authors

- **Nishkarsh Pandey** ⇒ [@Nish2005karsh](https://www.github.com/Nish2005karsh)


## 📎 Appendix

### A. Dataset Source  
The dataset used is the Telco Customer Churn dataset, widely used for churn prediction modeling.

Files used:  

- `train.csv`: for training and evaluation  
- `test.csv`: for testing and final model validation  

### B. Tools and Technologies  
**Language:** `Python 3.x` 🐍

**Libraries:**  
`pandas, numpy` — data manipulation and numerical computations  
`matplotlib, seaborn` — exploratory data analysis and visualization  
`scikit-learn` — model building and evaluation (Logistic Regression, Random Forest, etc.)  
`joblib` — model serialization  
`streamlit` — for deploying the predictive model as an interactive web app

**Development Environment:**  
`Jupyter Notebook` — for exploratory data analysis and prototyping  
`Visual Studio Code` — for development and project management  
`Web browser` — to run and interact with the Streamlit app locally or on a server


## Screenshots

![Streamlit_ss](Screenshots/streamlitss.png)

![Notebook_ss](Screenshots/notebook.png)


## Features

| Feature               | Type                  | Description                                                  |
| --------------------- | --------------------- | ------------------------------------------------------------ |
| `gender`              | Categorical           | Gender of the customer (`Male`, `Female`)                     |
| `SeniorCitizen`       | Binary                | Whether the customer is a senior citizen (0 = No, 1 = Yes)    |
| `Partner`             | Categorical           | Whether the customer has a partner (`Yes`, `No`)              |
| `Dependents`          | Categorical           | Whether the customer has dependents (`Yes`, `No`)             |
| `tenure`              | Numerical             | Number of months the customer has stayed with the company     |
| `PhoneService`        | Categorical           | Whether the customer has phone service (`Yes`, `No`)          |
| `MultipleLines`       | Categorical           | Whether customer has multiple phone lines                      |
| `InternetService`     | Categorical           | Customer’s internet service provider (`DSL`, `Fiber optic`, `No`) |
| `OnlineSecurity`      | Categorical           | Whether the customer has online security (`Yes`, `No`)        |
| `OnlineBackup`        | Categorical           | Whether the customer has online backup service (`Yes`, `No`)  |
| `DeviceProtection`    | Categorical           | Whether the customer has device protection (`Yes`, `No`)      |
| `TechSupport`         | Categorical           | Whether the customer has tech support (`Yes`, `No`)           |
| `StreamingTV`         | Categorical           | Whether the customer streams TV (`Yes`, `No`)                 |
| `StreamingMovies`     | Categorical           | Whether the customer streams movies (`Yes`, `No`)             |
| `Contract`            | Categorical           | Contract type (`Month-to-month`, `One year`, `Two year`)      |
| `PaperlessBilling`    | Categorical           | Whether the customer has paperless billing (`Yes`, `No`)      |
| `PaymentMethod`       | Categorical           | Payment method (`Electronic check`, `Mailed check`, etc.)     |
| `MonthlyCharges`      | Numerical             | The amount charged monthly                                    |
| `TotalCharges`        | Numerical             | Total amount charged to the customer                          |
| `Churn`               | Binary (Target)       | Whether the customer churned (`Yes` = churned, `No` = retained)|

