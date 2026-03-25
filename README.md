Car Price Prediction ML Project

This is an end-to-end Machine Learning project that predicts the selling price of a car based on various features like year, fuel type, transmission, and more.

Built as part of my **#100DaysOfML journey**

 Problem Statement
Car prices depend on multiple factors such as:
- Car age
- Fuel type
- Kilometers driven
- Transmission type

 Goal: Build a model that can accurately predict car selling price.

 Dataset
- Source: Aman Kharwal Dataset
- Features include:
  - Present_Price
  - Kms_Driven
  - Fuel_Type
  - Seller_Type
  - Transmission
  - Owner
  - Year



 Project Workflow

1. Data Loading  
2. Data Cleaning  
3. Feature Engineering  
4. Exploratory Data Analysis (EDA)  
5. Model Training  
6. Model Evaluation  
7. Model Saving  



 Models Used

- Linear Regression  
- Decision Tree  
- Random Forest (Best Model)  
- KNN  


 Results
- ✅ R² Score: **0.96**
- ✅ MAE: **0.61**
- ✅ RMSE: ~0.93  

 Random Forest performed the best.



 Tech Stack

- Python 🐍  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib & Seaborn  
- Joblib  



## 📁 Project Structure

car-price-project/
│
├── data/
│ └── car_price_prediction.csv
│
├── src/
│ ├── data_preprocessing.py
│ ├── model_training.py
│ └── evaluation.py
│
├── model/
│ └── car_price_model.pkl
│
├── main.py
├── app.py
├── requirements.txt
└── README.md

 How to Run
1. Clone the repository
2. Install dependencies
3. Run training pipeline
4. Run API



---

## 🌐 API Endpoint

After running FastAPI:

👉 Open: http://127.0.0.1:8000/docs  

You can test predictions directly from the browser.

---

## 💡 Key Learnings

- Building end-to-end ML pipeline  
- Feature engineering importance  
- Model comparison  
- Real-world ML workflow  
- Converting model into API  

---

## 📌 Future Improvements

- Hyperparameter tuning  
- Model deployment on cloud  
- Streamlit dashboard UI  
- Monitoring system  

🙌 Connect With Me

If you liked this project, feel free to connect and give feedback! 🚀  

⭐ Don’t forget to star this repo if you found it useful!
