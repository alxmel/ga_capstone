from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

MODEL_PATH = Path(__file__).parent.parent / "model" / "icepredictor.joblib"


class PredictionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_Alabama: int
    is_Arizona: int
    is_California: int
    is_Colorado: int
    is_Connecticut: int
    is_DC: int = Field(alias="is_D.C.")
    is_Florida: int
    is_Georgia: int
    is_Idaho: int
    is_Illinois: int
    is_Iowa: int
    is_Kansas: int
    is_Louisiana: int
    is_Maine: int
    is_Maryland: int
    is_Massachusetts: int
    is_Michigan: int
    is_Minnesota: int
    is_New_Jersey: int = Field(alias="is_New Jersey")
    is_New_York: int = Field(alias="is_New York")
    is_North_Carolina: int = Field(alias="is_North Carolina")
    is_Oklahoma: int
    is_Oregon: int
    is_Pennsylvania: int
    is_Tennessee: int
    is_Texas: int
    is_Utah: int
    is_Vermont: int
    is_Washington: int
    is_April: int
    is_August: int
    is_December: int
    is_February: int
    is_January: int
    is_July: int
    is_June: int
    is_March: int
    is_May: int
    is_November: int
    is_October: int
    is_September: int


@asynccontextmanager
async def lifespan(app: FastAPI):
    model = joblib.load(MODEL_PATH)
    app.state.model = model
    app.state.target_names = list(model.classes_)
    yield


app = FastAPI(
    title="P.R.E.D.I.C.T.I.C.E",
    version="1.0.0",
    description="GA Capstone",
    lifespan=lifespan,
)

@app.get("/")
def root():
    return {"message": "hello, ga capstone!"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        model = app.state.model
        target_names = app.state.target_names

        feature_data = request.model_dump(by_alias=True)
        df = pd.DataFrame([feature_data])[model.feature_names_in_]

        prediction_label = model.predict(df)[0]
        probabilities = model.predict_proba(df)[0]

        return {
            "prediction_label": prediction_label,
            "probabilities": {
                target_names[i]: float(round(probabilities[i], 2))
                for i in range(len(target_names))
            },
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
