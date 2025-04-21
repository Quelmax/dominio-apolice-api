from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.api.rota_apolice import rota

# Configura a aplicação de teste
app = FastAPI()
app.include_router(rota)

client = TestClient(app)

def test_criar_apolice_sucesso():
    # Dados de entrada válidos
    payload = {
        "cpf": "12345678909",
        "data_inicio": "2024-01-01",
        "data_fim": "2027-01-01",
        "valor_premio": 1000.0
    }

    # Envia a requisição POST
    response = client.post("/apolice", json=payload)

    # Verifica o status da resposta
    assert response.status_code == 201

    # Verifica os dados retornados
    data = response.json()
    assert data["cpf"] == payload["cpf"]
    assert data["data_inicio"] == payload["data_inicio"]
    assert data["data_fim"] == payload["data_fim"]
    assert data["valor_premio"] == payload["valor_premio"]

def test_criar_apolice_cpf_invalido():
    # Dados de entrada com CPF inválido
    payload = {
        "cpf": "123",
        "data_inicio": "2023-01-01",
        "data_fim": "2024-01-01",
        "valor_premio": 1000.0
    }

    # Envia a requisição POST
    response = client.post("/apolice", json=payload)

    # Verifica o status da resposta
    assert response.status_code == 400

    # Verifica a mensagem de erro
    data = response.json()
    assert "CPF inválido" in data["detail"]

def test_criar_apolice_data_invalida():
    # Dados de entrada com data inválida
    payload = {
        "cpf": "12345678909",
        "data_inicio": "2024-01-01",
        "data_fim": "2023-01-01",
        "valor_premio": 1000.0
    }

    # Envia a requisição POST
    response = client.post("/apolice", json=payload)

    # Verifica o status da resposta
    assert response.status_code == 400

    # Verifica a mensagem de erro
    data = response.json()
    assert "A data de início deve ser anterior ou igual à data de fim." in data["detail"]