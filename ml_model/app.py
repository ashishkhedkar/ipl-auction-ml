from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request Model

class PlayerInput(BaseModel):
    strike_rate: float
    matches: int


# Health Check Route

@app.get("/")
def home():
    return {"message": "IPL API Running 🚀"}



# Prediction Route

@app.post("/predict")
def predict(data: PlayerInput):
    try:
        # Import inside function (IMPORTANT)
        from train_model import predict_runs

        result = predict_runs(data.strike_rate, data.matches)
        return {"predicted_runs": result}

    except Exception as e:
        return {
            "error": "Prediction failed",
            "details": str(e)
        }