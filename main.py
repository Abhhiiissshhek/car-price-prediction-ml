import joblib
from data_preprocessing import load_data, preprocess_data
from model_training import train_model
from evaluation import evaluate_model

# Load data
df = load_data("data/car_price_prediction.csv")

# Preprocess
df = preprocess_data(df)

# Train model
model, X_test, y_test = train_model(df)

# Evaluate
mae, rmse, r2 = evaluate_model(model, X_test, y_test)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Save model
joblib.dump(model, "model/car_price_model.pkl")

print("Model saved successfully!")