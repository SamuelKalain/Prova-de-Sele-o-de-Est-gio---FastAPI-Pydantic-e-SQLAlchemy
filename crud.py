from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria 
from schemas import EmpresaCreate, ObrigacaoAcessoriaCreate 


def criar_empresa(db: Session, empresa: EmpresaCreate):
    db_empresa = Empresa(nome=empresa.nome, cnpj=empresa.cnpj, endereco=empresa.endereco)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa 


def obter_empresa(db: Session, empresa_id: int):
    return db.query(Empresa).filter(Empresa.id == empresa_id).first()

def listar_empresas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Empresa).offset(skip).limit(limit).all()  


def criar_obrigacao(db: Session, obrigacao: ObrigacaoAcessoriaCreate):
    db_obrigacao = ObrigacaoAcessoria(
        nome=obrigacao.nome,
        periodicidade=obrigacao.periodicidade,
        empresa_id=obrigacao.empresa_id
    )
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

def listar_obrigacoes(db: Session, empresa_id: int):
    return db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.empresa_id == empresa_id).all()

def obter_obrigacao(db: Session, obrigacao_id: int):
    return db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
