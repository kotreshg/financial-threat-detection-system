# Financial Threat Detection System

A machine learning-based financial threat detection system that uses
XGBoost to classify financial transactions as fraudulent or secure.
The trained model is integrated with a Flask web application that
simulates transaction scanning and displays the predicted risk,
transaction details, and threat information.

## Features

- Financial transaction fraud detection using XGBoost
- Data preprocessing and feature scaling
- Stratified 80/20 train-test split
- Class-imbalance handling using `scale_pos_weight`
- Model evaluation using classification report and confusion matrix
- Saved trained model using Joblib
- Flask-based web interface
- Simulated fraud and normal transaction scanning
- Risk score generation
- Transaction metadata and threat-reason display

## Technologies Used

- Python
- XGBoost
- Scikit-learn
- Pandas
- NumPy
- Flask
- Matplotlib
- Seaborn
- Joblib
- HTML/CSS

## Machine Learning Pipeline

The system follows this workflow:

1. Load the Credit Card Fraud Detection dataset.
2. Scale the `Time` and `Amount` features using `StandardScaler`.
3. Remove the original `Time` and `Amount` columns.
4. Separate the features and target (`Class`).
5. Split the data into 80% training and 20% testing sets using
   stratification.
6. Train an XGBoost classification model.
7. Evaluate the model using classification metrics and a confusion matrix.
8. Save the trained model as `xgboost_fraud_model.joblib`.
9. Save the test data as `live_test_data.csv` for the Flask application.

## Project Structure

financial_threat_detection/
│
├── dataset/
│   └── README.md
│
├── static/
│   └── threat_detection_matrix.png
│
├── templates/
│   └── index.html
│
├── app.py
├── data_preprocessing.py
├── main.py
├── model_trainer.py
├── xgboost_fraud_model.joblib
├── requirements.txt
├── how_to_run.txt
├── .gitignore
└── README.md
Dataset
This project uses the Credit Card Fraud Detection dataset
available on Kaggle.
The original creditcard.csv file is not included in this repository
because of its large file size.
Download the dataset and place it at:
dataset/creditcard.csv
The dataset should contain the transaction features and the Class
column, where the class is used as the fraud target.
Installation
Clone the repository and install the required Python packages:
pip install -r requirements.txt
Running the Project
1. Add the dataset
Place the downloaded creditcard.csv file inside:
dataset/
2. Train the model
Run:
python main.py
This performs preprocessing, trains and evaluates the XGBoost model,
and generates the trained model and test data required by the Flask
application.
3. Start the Flask application
Run:
python app.py
Open the local URL displayed in the terminal in a web browser.
Model Evaluation
The training pipeline generates a classification report and a
confusion matrix to evaluate fraud detection performance.
The confusion matrix is saved as:
static/threat_detection_matrix.png
Web Application
The Flask application provides a transaction scanning interface.
Transactions can be simulated as either normal or fraudulent, after
which the trained XGBoost model generates a prediction and risk score.
The application also displays simulated transaction metadata such as:
Transaction ID
Transaction amount
Location
Device
IP address
Prediction
Risk score
Threat reason

```text

<img width="2926" height="1326" alt="WhatsApp Image 2026-09-18 at 15 41 35" src="https://github.com/user-attachments/assets/1b917dc2-94d2-45de-9081-de2b67ffe5a6" />

<img width="2912" height="1456" alt="WhatsApp Image 2026-09-18 at 15 41 15" src="https://github.com/user-attachments/assets/ac784365-e59a-427a-ad77-b18f2bca0642" />

<img width="2934" height="1196" alt="WhatsApp Image 2026-09-18 at 15 40 55" src="https://github.com/user-attachments/assets/26da43b3-8b9f-4143-b598-a6f712765b2e" />

<img width="2928" height="1422" alt="WhatsApp Image 2026-09-18 at 15 40 27" src="https://github.com/user-attachments/assets/6950216a-e55f-42a8-a19c-d483e22d9569" />

<img width="1280" height="682" alt="image" src="https://github.com/user-attachments/assets/c8b3af12-003a-434d-b399-93f28afbd6c1" />
