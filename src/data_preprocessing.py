import pandas as pd

DATA_PATH = "data/car_price_prediction.csv"
df = load_data(DATA_PATH)

def preprocess_data(df):
    # Feature Engineering
    df['Car_Age'] = 2024 - df['Year']

    # Drop unnecessary columns
    df.drop(['Car_Name', 'Year'], axis=1, inplace=True)

    # Encode categorical variables
    df = pd.get_dummies(df, drop_first=True)

    return df