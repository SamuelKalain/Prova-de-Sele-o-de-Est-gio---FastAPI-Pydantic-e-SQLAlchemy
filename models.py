from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    endereco = Column(String)
    email = Column(String)  
    telefone = Column(String)  
    
    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")

    def __repr__(self):
        return f"<Empresa(nome={self.nome}, cnpj={self.cnpj}, endereco={self.endereco}, email={self.email}, telefone={self.telefone})>"

class ObrigacaoAcessoria(Base):
    __tablename__ = 'obrigacoes_acessorias'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    periodicidade = Column(String)  
    empresa_id = Column(Integer, ForeignKey('empresas.id'))

    
    empresa = relationship("Empresa", back_populates="obrigacoes")

    def __repr__(self):
        return f"<ObrigacaoAcessoria(nome={self.nome}, periodicidade={self.periodicidade}, empresa_id={self.empresa_id})>"
