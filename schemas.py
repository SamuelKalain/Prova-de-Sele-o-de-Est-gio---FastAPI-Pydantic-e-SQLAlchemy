from pydantic import BaseModel
from typing import List

class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class Empresa(EmpresaCreate):
    id: int
    obrigacoes: List["ObrigacaoAcessoria"] = []

    class Config:
        orm_mode = True

class ObrigacaoAcessoriaCreate(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoAcessoria(ObrigacaoAcessoriaCreate):
    id: int

    class Config:
        orm_mode = True
