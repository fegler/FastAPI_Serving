import logging 
import logging.config 
import os 

from fastapi import FastAPI
from app.api.endpoints import router

if not os.path.exists("logs"):
    os.mkdir("logs")

logging.config.fileConfig("logging.conf")
logger = logging.getLogger() 

app = FastAPI()
predictor = Predictor() 

@app.get("/health-check")
def healthcheck() -> bool:
    """Check the server's status"""
    return True 

@app.get("/predict-ocr")
async def predict_ocr(data):
    logger.info("Received an image")
    prediction = await predictor.predict(data.image, data.height, data.width)
    