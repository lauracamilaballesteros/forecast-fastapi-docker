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
    return joblib.load('/app/model.joblib')


def test_predict_sale_amount(client, model):
    # cargar un conjunto de datos de prueba
    test_data = [{"fecha": "2009-01-01"}, {"fecha": "2009-01-02"}, {"fecha": "2009-01-03"}]
    expected_result = 100.0 # Valor esperado para comparar con el resultado de la predicción

    # enviar una solicitud POST al endpoint de predicción con los datos de prueba
    response = client.post('/predict', json={'data': test_data})

    # verificar que la solicitud tuvo éxito y devolvió un código de estado HTTP 200
    assert response.status_code == 200

    # verificar que el resultado de la predicción coincide con el valor esperado
    assert response.json()[0]['ventas_pred'] == expected_result
