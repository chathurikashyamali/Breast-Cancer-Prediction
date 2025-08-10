🔬 Breast Cancer Diagnosis Prediction App
An interactive Streamlit web application that predicts whether a breast tumor is benign or malignant based on medical measurements.
This project uses a trained Machine Learning model built with Scikit-learn and is intended for educational purposes only (not for medical diagnosis).

📌 Features
User-friendly interface for entering tumor feature values.

ML Model trained on a breast cancer dataset.

Automatic feature scaling for accurate predictions.

Clear visual feedback:

✅ Benign (Non-cancerous)

⚠️ Malignant (Cancerous)

Fast predictions using pre-saved model and scaler with Joblib.

🛠 Tech Stack
Python

Pandas, NumPy – Data handling and processing

Scikit-learn – Model training and evaluation

Joblib – Model persistence

Streamlit – Web application framework

📂 Project Structure
bash
Copy
Edit
Breast-Cancer-Prediction/
│
├── app.py                  # Main Streamlit app
├── breast_cancer_model.pkl # Trained ML model
├── scaler.pkl              # Feature scaler
├── data/                   # Dataset (optional, if included)
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
🚀 How to Run the App Locally
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/chathurikashyamali/Breast-Cancer-Prediction.git
cd Breast-Cancer-Prediction
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit app
bash
Copy
Edit
python -m streamlit run app.py
4️⃣ Open in browser
The app will open automatically at:

arduino
Copy
Edit
http://localhost:8501
📊 Dataset
The model is trained on the Breast Cancer Wisconsin (Diagnostic) Dataset from Kaggle.

⚠️ Disclaimer
This tool is not a substitute for professional medical advice.
It is intended solely for educational and demonstration purposes.

🏆 Skills Gained
Python programming

Data preprocessing & feature scaling

Machine learning model training (classification)

Model deployment with Streamlit

Git & GitHub project management

