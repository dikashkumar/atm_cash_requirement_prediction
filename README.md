# 💳 ATM Cash Requirement Prediction using Machine Learning

<div align="center">

### 🚀 Smart ATM Cash Forecasting System

Predict ATM cash requirements efficiently using Machine Learning and Flask.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge\&logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Linear%20Regression-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

---

## 📖 About The Project

Managing ATM cash efficiently is a major challenge for banks. Excess cash increases operational costs, while insufficient cash leads to customer dissatisfaction.

This project uses **Machine Learning (Linear Regression)** to predict the amount of cash required in an ATM based on:

* Current ATM Cash
* Customer Withdrawals

The system helps optimize cash replenishment and reduce ATM downtime.

---

## 🎯 Problem Statement

Banks often face:

✅ ATM cash shortages

✅ Unnecessary cash loading

✅ Poor cash distribution planning

✅ Increased maintenance costs

This project aims to provide a smart prediction system that helps maintain the right amount of cash in ATMs.

---

## ⚡ Features

* 💰 Predict ATM Cash Requirement
* 📊 Machine Learning-Based Forecasting
* 🏦 ATM Balance Calculation
* 🌐 Interactive Flask Web Application
* ⚡ Instant Prediction Results
* 📱 Responsive User Interface
* 🔍 Easy Data Analysis

---

## 🛠️ Technology Stack

| Technology        | Purpose             |
| ----------------- | ------------------- |
| Python            | Backend Development |
| Flask             | Web Framework       |
| Pandas            | Data Processing     |
| Scikit-Learn      | Machine Learning    |
| HTML/CSS          | Frontend UI         |
| Linear Regression | Prediction Model    |

---

## 📂 Project Structure

```text
ATM-Cash-Requirement-Prediction/
│
├── app.py
├── atm_data.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 🤖 Machine Learning Model

### Input Features

| Feature    | Description                 |
| ---------- | --------------------------- |
| Total_Cash | Total cash available in ATM |
| Withdrawal | Cash withdrawn by customers |

### Output

| Output        | Description                |
| ------------- | -------------------------- |
| Required_Cash | Predicted cash requirement |

### Algorithm Used

**Linear Regression**

The model learns from historical ATM transaction data and predicts future cash requirements.

---

## 🔄 Working Process

```text
User Input
     ↓
ATM Details
     ↓
Current Cash
     ↓
Withdrawal Amount
     ↓
Machine Learning Model
     ↓
Cash Requirement Prediction
     ↓
Display Results
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ATM-Cash-Requirement-Prediction.git
```

### Navigate to Project Folder

```bash
cd ATM-Cash-Requirement-Prediction
```

### Install Dependencies

```bash
pip install flask pandas scikit-learn
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📸 Sample Prediction

### Input

| Parameter  | Value  |
| ---------- | ------ |
| ATM ID     | ATM001 |
| Total Cash | 500000 |
| Withdrawal | 150000 |

### Output

| Result                  | Value            |
| ----------------------- | ---------------- |
| Remaining Balance       | 350000           |
| Predicted Required Cash | Model Prediction |

---

## 🌟 Future Enhancements

* 📈 Advanced Forecasting Models
* 🗄️ Database Integration
* ☁️ Cloud Deployment
* 📊 Analytics Dashboard
* 📍 Multi-ATM Monitoring
* 🔔 Cash Refill Alerts
* 🤖 AI-Based Demand Forecasting

---

## 🎓 Academic Relevance

This project demonstrates:

* Machine Learning Fundamentals
* Regression Analysis
* Flask Web Development
* Data Processing using Pandas
* Real-world Banking Applications

---

## 👨‍💻 Developer

### Dikash Kumar S

🎓 Computer Science Engineering Student

💡 Machine Learning Enthusiast

🐍 Python Developer

🚀 Passionate about AI, Data Science and Full Stack Development

---

<div align="center">

### ⭐ Star this repository if you found it useful!

"Using Machine Learning to make ATM cash management smarter and more efficient."

</div>
