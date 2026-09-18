import os
from flask import Flask, render_template, jsonify
import joblib
import pandas as pd
import random

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'xgboost_fraud_model.joblib')
DATA_PATH = os.path.join(BASE_DIR, 'dataset', 'live_test_data.csv')

print("Loading AI Model...")
if not os.path.exists(MODEL_PATH):
    print(f"\n[ERROR] Model file not found at: {MODEL_PATH}")
    exit()

model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

frauds = df[df['Actual_Class'] == 1]
normals = df[df['Actual_Class'] == 0]

def generate_metadata():
    locations = ['Mumbai, MH', 'Bengaluru, KA', 'Delhi, DL', 'Hyderabad, TG', 'Chennai, TN', 'Pune, MH']
    devices = ['iOS App', 'Android App', 'Web Portal', 'UPI Gateway', 'ATM API']
    base = random.random() ** 3 
    realistic_amount = 100.00 + (214900.00 * base) 
    
    return {
        'amount': round(realistic_amount, 2),
        'location': random.choice(locations),
        'device': random.choice(devices),
        'ip': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    }

# NEW: Generate realistic SOC Analyst reasons for blocked transactions
def generate_fraud_reason():
    reasons = [
        "Velocity Anomaly: Impossible travel distance between consecutive IP geographic locations.",
        "Device Fingerprint Mismatch: Attempted access from unregistered/unrecognized hardware.",
        "Network Routing Flagged: Traffic routed through known malicious VPN or Botnet subnet.",
        "Behavioral Anomaly: Transaction velocity exceeds 99th percentile of user's historical baseline.",
        "Authentication Bypass Attempt: Irregular payload detected in API header sequence."
    ]
    return random.choice(reasons)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan/<transaction_type>')
def scan_transaction(transaction_type):
    if transaction_type == 'fraud':
        sample = frauds.sample(1)
    else:
        sample = normals.sample(1)
        
    actual_class = int(sample['Actual_Class'].values[0])
    features = sample.drop('Actual_Class', axis=1)
    
    probability = float(model.predict_proba(features)[0][1])
    prediction = 1 if probability > 0.5 else 0
    
    metadata = generate_metadata()
    
    # Attach the reason if it's a fraud
    threat_reason = generate_fraud_reason() if prediction == 1 else "Normal behavioral pattern verified."
    
    return jsonify({
        'transaction_id': f"TXN-{random.randint(1000000, 9999999)}",
        'prediction': "FRAUD" if prediction == 1 else "SECURE",
        'risk_score': round(probability * 100, 2),
        'amount': metadata['amount'],
        'location': metadata['location'],
        'device': metadata['device'],
        'ip_address': metadata['ip'],
        'reason': threat_reason # Sending the reason to the frontend
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)