import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
from xgboost import XGBRegressor
import pickle



data = pd.read_csv('ML-DL-Projects/House_Price_Prediction in Streamlit/feature_engineered_data.csv')
print(data.head(3))
print(data.info())
# Split the data into train and test
X = data.drop(['median_house_value'],  axis = 1)
Y = data['median_house_value']
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state=0)

# Trying Differenr Models
forest = RandomForestRegressor(n_estimators=300)
forest.fit(train_X, train_Y)
print(f"Forest Score: {forest.score(test_X, test_Y)}")


# XGBoost

X = data.drop(['median_house_value'],  axis = 1)
Y = data['median_house_value']
X.rename(columns={'<1H OCEAN': 'In OCEAN'}, inplace=True)
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state=0)
xgb = XGBRegressor(random_state=0)
xgb.fit(train_X, train_Y)
print(f"XGBoost Score: {xgb.score(test_X, test_Y)}")

# Random Forest Score ~ 81
# XGBoost Score ~ 82 + Faster
# ---------- XGBoost Performed Well ----------

# Save the model using pickle

joblib.dump(xgb , 'model_jlib')
