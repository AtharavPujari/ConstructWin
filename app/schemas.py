from pydantic import BaseModel

class InputData(BaseModel):
    area: float
    floors: int
    workers: int
    delay_days: int
    weather_risk: str
