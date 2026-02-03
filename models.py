from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    perfil = relationship("Perfil", back_populates = "estudante", uselist = False, cascade = "all, delete-orphan")
    
class Perfil(Base):
    __tablename__ = 'perfis'
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    nome_mae = Column(String)
    nome_pai = Column(String)
    numero_emergencia = Column(Integer)
    estudantes_id = Column(Integer, ForeignKey("estudantes.id"), unique=True)
    estudante = relationship("Estudante", back_populates = "perfil")

class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    materias = Column(String)
    email = Column(String)
    numero = Column(Integer)

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    servico = Column(String)
    email = Column(String)
    numero = Column(Integer)

    