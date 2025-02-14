from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Testes 
def setup_module(module):
    response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste Setup",
            "cnpj": "22345678000195",
            "endereco": "Rua Setup, 123",
            "email": "empresa@setup.com",
            "telefone": "0987654321"
        }
    )
    assert response.status_code == 200

def teardown_module(module):
    
    pass

def test_criar_empresa():
    response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678000195",
            "endereco": "Rua Teste, 123",
            "email": "empresa@teste.com",
            "telefone": "1234567890"
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"


def test_listar_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_obter_empresa():
    response = client.get("/empresas/1")
    assert response.status_code in [200, 404] 

def test_atualizar_empresa():
    response = client.put(
        "/empresas/1",
        json={
            "nome": "Empresa Atualizada",
            "cnpj": "12345678000195",
            "endereco": "Rua Atualizada, 123",
            "email": "empresa@atualizada.com",
            "telefone": "1234567890"
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Atualizada"

def test_excluir_empresa():
    response = client.delete("/empresas/1")
    assert response.status_code == 200

def test_criar_obrigacao():
    response = client.post(
        "/obrigacoes/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": 1
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Obrigação Teste"

def test_listar_obrigacoes():
    response = client.get("/empresas/1/obrigacoes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_obter_obrigacao():
    response = client.get("/obrigacoes/1")
    assert response.status_code in [200, 404]  

def test_atualizar_obrigacao():
    response = client.put(
        "/obrigacoes/1",
        json={
            "nome": "Obrigação Atualizada",
            "periodicidade": "anual",
            "empresa_id": 1
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Obrigação Atualizada"

def test_excluir_obrigacao():
    response = client.delete("/obrigacoes/1")
    assert response.status_code == 200
