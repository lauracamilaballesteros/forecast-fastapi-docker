from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import joblib
import pandas as pd
import statsmodels.api as sm
from typing import List


filename = 'D:/Github/Proyecto-MLE/forecast-fastapi-docker/notebooks/model.joblib'
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

    return out

app.include_router(router)