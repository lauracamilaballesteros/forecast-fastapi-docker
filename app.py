

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import joblib
import pandas as pd
import statsmodels.api as sm
from typing import List
import json
from starlette.responses import JSONResponse



filename = '/app/model.joblib'
clf = joblib.load(filename)


class DataIn(BaseModel):
    fecha: List[str]


app = FastAPI()
router = APIRouter()


@router.post("/predict")
async def predict(data: DataIn):
    df_in = pd.DataFrame(data.fecha, columns=['fecha'])
    df_in['fecha'] = pd.to_datetime(df_in['fecha'])
    
    last_date = df_in['fecha'].max()
    idx = pd.date_range(start=last_date, periods=7, freq='D')
    pred = clf.forecast(steps=7)
    
    df_out = pd.DataFrame(idx, columns=['fecha'])
    df_out['ventas_pred'] = pred
    
    out = df_out.to_dict(orient='records')

    # Formatear los valores de punto flotante
    for item in out:
        item['ventas_pred'] = round(item['ventas_pred'], 2)

    # Convertir a JSON y devolver la respuesta
    response = json.dumps(out)
    return JSONResponse(response)
    


@app.get("/")
async def root():
    return "The quality is good"




app.include_router(router)
