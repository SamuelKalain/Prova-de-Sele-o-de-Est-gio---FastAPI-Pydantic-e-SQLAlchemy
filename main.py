from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, FileResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Empresa as EmpresaModel, ObrigacaoAcessoria as ObrigacaoAcessoriaModel
from schemas import EmpresaCreate, Empresa, ObrigacaoAcessoriaCreate, ObrigacaoAcessoria
from crud import criar_empresa, obter_empresa, listar_empresas, criar_obrigacao, listar_obrigacoes, obter_obrigacao
from typing import List

# Criar as tabelas do banco de dados
EmpresaModel.metadata.create_all(bind=engine)
ObrigacaoAcessoriaModel.metadata.create_all(bind=engine)

app = FastAPI()

# Função para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para a página inicial personalizada
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("index.html")

# Rotas para Empresas
@app.post("/empresas/", response_model=Empresa)
def criar_empresa_route(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    return criar_empresa(db=db, empresa=empresa)

@app.get("/empresas/{empresa_id}", response_model=Empresa)
def obter_empresa_route(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = obter_empresa(db=db, empresa_id=empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.get("/empresas/", response_model=List[Empresa])
def listar_empresas_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return listar_empresas(db=db, skip=skip, limit=limit)

@app.put("/empresas/{empresa_id}", response_model=Empresa)
def atualizar_empresa_route(empresa_id: int, empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = obter_empresa(db=db, empresa_id=empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    db_empresa.nome = empresa.nome
    db_empresa.cnpj = empresa.cnpj
    db_empresa.endereco = empresa.endereco
    db_empresa.email = empresa.email
    db_empresa.telefone = empresa.telefone
    db.commit()
    db.refresh(db_empresa)
    return db_empresa


@app.delete("/empresas/{empresa_id}", response_model=Empresa)
def excluir_empresa_route(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = obter_empresa(db=db, empresa_id=empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    db.delete(db_empresa)
    db.commit()
    return db_empresa

# Rotas para Obrigações Acessórias
@app.post("/obrigacoes/", response_model=ObrigacaoAcessoria)
def criar_obrigacao_route(obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return criar_obrigacao(db=db, obrigacao=obrigacao)

@app.get("/obrigacoes/{obrigacao_id}", response_model=ObrigacaoAcessoria)
def obter_obrigacao_route(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = obter_obrigacao(db=db, obrigacao_id=obrigacao_id)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return db_obrigacao

@app.get("/empresas/{empresa_id}/obrigacoes", response_model=List[ObrigacaoAcessoria])
def listar_obrigacoes_route(empresa_id: int, db: Session = Depends(get_db)):
    return listar_obrigacoes(db=db, empresa_id=empresa_id)

@app.put("/obrigacoes/{obrigacao_id}", response_model=ObrigacaoAcessoria)
def atualizar_obrigacao_route(obrigacao_id: int, obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = obter_obrigacao(db=db, obrigacao_id=obrigacao_id)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    db_obrigacao.nome = obrigacao.nome
    db_obrigacao.periodicidade = obrigacao.periodicidade
    db_obrigacao.empresa_id = obrigacao.empresa_id
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.delete("/obrigacoes/{obrigacao_id}", response_model=ObrigacaoAcessoria)
def excluir_obrigacao_route(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = obter_obrigacao(db=db, obrigacao_id=obrigacao_id)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    db.delete(db_obrigacao)
    db.commit()
    return db_obrigacao
