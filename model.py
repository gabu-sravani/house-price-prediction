import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle

# Sample dataset (replace with your dataset if you have one)
data = {
    'sqft': [800, 1000, 1200, 1500, 1800, 2000],
    'rooms': [2, 2, 3, 3, 4, 4],
    'interior': [1, 1, 2, 2, 2, 1],   # 1 = Normal, 2 = Good
    'exterior': [1, 2, 2, 1, 2, 2],   # 1 = Normal, 2 = Good
    'material': [1, 2, 2, 1, 2, 2],   # 1 = Normal, 2 = High
    'quality': [1, 1, 2, 2, 3, 3],    # 1 = Low, 2 = Medium, 3 = High
    'price': [3000000, 4000000, 5000000, 6500000, 8000000, 9000000]
}

df = pd.DataFrame(data)

X = df.drop('price', axis=1)
y = df['price']

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as model.pkl")