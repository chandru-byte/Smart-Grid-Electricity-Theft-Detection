# ⚡ Smart Grid Electricity Theft Detection

🚀 AI-powered system to detect electricity theft using real-time monitoring and machine learning.

---

## 🔍 Overview

This project monitors electricity usage and detects abnormal patterns that indicate possible theft.

👉 Uses a **Random Forest model** to classify:

* `0 → Normal Usage`
* `1 → Electricity Theft`

---

## 📸 Dashboard Preview

### 🟢 Normal Monitoring

<img width="938" height="535" alt="Screenshot 2026-04-07 221004" src="https://github.com/user-attachments/assets/9d5ec6ac-bc43-41b9-aa19-f665597cf6ef" />


### 🔴 Theft Detection Alert

<img width="1892" height="1077" alt="Screenshot 2026-04-07 221848" src="https://github.com/user-attachments/assets/42266902-c44c-4939-aa09-c5a877242907" />


---

## ⚙️ Features

✔ Real-time electricity monitoring
✔ Theft detection using Machine Learning
✔ Live dashboard with status indicators
✔ Theft alert (popup + UI alert)
✔ Email notification system
✔ Login authentication system

---

## 🧠 Machine Learning

* Model: **Random Forest Classifier**
* Input: Last **200-day electricity usage**
* Output:

  * Normal / Theft prediction
  * Confidence score
  * Theft probability

---

## 🖥️ System Architecture

* Frontend → Interactive dashboard (HTML, CSS, JS) 
* Backend → Flask API for prediction & login 
* ML Model → Trained using Scikit-learn
* Dependencies → 

---

## 🔐 Login

Simple authentication system: 

```
Username: customer1  
Password: 1234
```

---

## 🌐 Live Demo

👉 https://smart-grid-8kqd.onrender.com/

---

## 🔄 Workflow

1. User logs in
2. Dashboard starts monitoring
3. Electricity usage data is analyzed
4. ML model predicts usage pattern
5. If theft detected:

   * UI alert shown 🔴
   * Popup alert triggered
   * Email sent 📧

---

## 🚨 Detection Logic

The system detects theft based on:

* Sudden spike in power usage
* Zero consumption (meter bypass)
* Abnormal consumption patterns

---

## 📁 Project Structure

```
├── app.py
├── smart-grid-dashboard.html
├── login.html
├── requirements.txt
└── smart_grid_pipeline.pkl
```

---

## 💡 Future Improvements

* Add XGBoost / LSTM models
* IoT smart meter integration
* Mobile notifications
* Advanced analytics dashboard

---

## 👨‍💻 Author

Chandru

---

🔥 *“Smart Monitoring. Smart Detection.”*
