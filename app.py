from flask import Flask, request, jsonify, send_from_directory, session, send_file
from flask_cors import CORS
import numpy as np
import os
import logging
from collections import deque
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# -------- EMAIL ALERT --------

def send_email_alert():
    sender="chandruv2004gbhss@gmail.com"
    password="tgbf tveu jjnd oqjk"
    receiver="chandruvenkat30@gmail.com"

    msg=MIMEText("⚠ Electricity Theft Detected")
    msg["Subject"]="Smart Grid Alert"
    msg["From"]=sender
    msg["To"]=receiver

    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(sender,password)
    server.sendmail(sender,receiver,msg.as_string())
    server.quit()

send_email_alert()
# -------- CONFIG --------

PIPELINE_PATH="smart_grid_pipeline.pkl"
N_FEATURES=200

app=Flask(__name__,static_folder=".")
app.secret_key="smartgrid123"
CORS(app)

reading_history=deque(maxlen=500)
pipeline=None

# -------- LOAD MODEL --------

def load_model():
    global pipeline
    try:
        import joblib
        pipeline=joblib.load(PIPELINE_PATH)
        print("Model loaded")
    except Exception as e:
        print("Model load error:",e)

load_model()

# -------- ML --------

LABEL_MAP={0:"Normal Usage",1:"Electricity Theft Detected"}

def run_prediction(features):
    arr=np.array(features).reshape(1,N_FEATURES)

    pred=int(pipeline.predict(arr)[0])
    proba=pipeline.predict_proba(arr)[0]

    return{
        "prediction":pred,
        "label":LABEL_MAP[pred],
        "confidence":round(float(max(proba)),4),
        "theft_probability":round(float(proba[1]),4)
    }

# -------- LOGIN --------

users={
    "customer1":"1234"
}

@app.route("/login",methods=["POST"])
def login():
    data=request.get_json()

    if data["username"] in users and users[data["username"]]==data["password"]:
        session["user"]=data["username"]
        return jsonify({"status":"success"})

    return jsonify({"status":"fail"})

# -------- DASHBOARD --------

@app.route("/")
def index():

    if "user" not in session:
        return send_file("login.html")

    return send_file("smart-grid-dashboard.html")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return send_file("login.html")

# -------- PREDICT --------

@app.route("/predict",methods=["POST"])
def predict():

    body=request.get_json(silent=True)

    if not body or "data" not in body:
        return jsonify({"error":"Missing data"}),400

    data=body["data"]

    if len(data)!=N_FEATURES:
        return jsonify({"error":"Need 200 values"}),400

    try:
        features=[float(x) for x in data]
    except:
        return jsonify({"error":"Invalid data"}),400

    try:
        result=run_prediction(features)
    except:
        return jsonify({"error":"Prediction failed"}),500

    if result["prediction"]==1:
        send_email_alert()

    reading_history.append({
        "time":datetime.utcnow().isoformat(),
        "prediction":result["prediction"],
        "label":result["label"]
    })

    return jsonify(result)

@app.route("/history")
def history():
    return jsonify(list(reading_history))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
  