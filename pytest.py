import pytest
import joblib
import pandas as pd

from fastapi.testclient import TestClient
from app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def model():
    return joblib.load('D:/Github/Proyecto-MLE/forecast-fastapi-docker/notebooks/model.joblib')


def test_predict_sale_amount(client, model):
    # cargar un conjunto de datos de prueba
    test_data = pd.read_csv('D:/Github/Proyecto-MLE/forecast-fastapi-docker/notebooks/model/datos-prueba.csv')
    expected_result = 100.0 # Valor esperado para comparar con el resultado de la predicción

    # enviar una solicitud POST al endpoint de predicción con los datos de prueba
    response = client.post('/predict', json={'data': test_data.to_dict(orient='records')})

    # verificar que la solicitud tuvo éxito y devolvió un código de estado HTTP 200
    assert response.status_code == 200

    # verificar que el resultado de la predicción coincide con el valor esperado
    assert response.json()[0]['prediction'] == expected_result
