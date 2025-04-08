from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from app.schemas import InputData
from app.recommend import generate_recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
cost_model = load("app/models/cost_model.pkl")
time_model = load("app/models/time_model.pkl")
risk_model = load("app/models/safety_model.pkl")

@app.post("/predict")
def predict(data: InputData):
    input_values = [[
        data.area,
        data.floors,
        data.workers,
        data.delay_days,
        1 if data.weather_risk.lower() == "high" else 0
    ]]

    cost = cost_model.predict(input_values)[0]
    time = time_model.predict(input_values)[0]
    risk = risk_model.predict(input_values)[0]

    risk_label = "Low"
    if risk > 0.6:
        risk_label = "High"
    elif risk > 0.3:
        risk_label = "Medium"

    return {
        "predicted_cost": round(cost, 2),
        "predicted_time_days": round(time, 2),
        "safety_risk": risk_label
    }

@app.post("/recommend")
def recommend(data: InputData):
    recommendations = generate_recommendations(
        data.area, data.floors, data.workers,
        data.delay_days, data.weather_risk
    )
    return {"recommendations": recommendations}
