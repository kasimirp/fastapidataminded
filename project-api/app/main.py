import os
from random import gauss

from fastapi import FastAPI
import uvicorn

app = FastAPI()

TARGET_PORT = os.environ.get("PORT", 8080)


@app.get("/")
def read_root():
    return {"Goodbye": "People"}


@app.get("/get_prediction")
def get_prediction(feature_a: float, feature_b: float):
    return {"predictions": [gauss(mu=feature_a, sigma=feature_b),
                            gauss(mu=feature_a, sigma=feature_b)]}


if __name__ == '__main__':
    uvicorn.run(app, port=TARGET_PORT, host='0.0.0.0')
