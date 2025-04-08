import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import joblib

# Generate fake data
df = pd.DataFrame({
    'area': np.random.randint(100, 5000, 1000),
    'floors': np.random.randint(1, 20, 1000),
    'workers': np.random.randint(10, 200, 1000),
    'weather_risk': np.random.randint(0, 2, 1000),
    'material_delay_days': np.random.randint(0, 10, 1000),
})

# Targets
df['cost'] = df['area'] * 150 + df['floors'] * 10000 + df['material_delay_days'] * 5000
df['time'] = df['floors'] * 5 + df['material_delay_days'] * 2 + 30
df['safety_risk'] = ((df['workers'] < 30) | (df['weather_risk'] == 1)).astype(int)

# Train and save
X = df.drop(columns=['cost', 'time', 'safety_risk'])
joblib.dump(RandomForestRegressor().fit(X, df['cost']), "app/models/cost_model.pkl")
joblib.dump(RandomForestRegressor().fit(X, df['time']), "app/models/time_model.pkl")
joblib.dump(RandomForestClassifier().fit(X, df['safety_risk']), "app/models/safety_model.pkl")
