from typing import List, Optional
from pydantic import BaseModel

class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str
    nome_mae: str
    nome_pai: str
    numero_emergencia: int

    
    class Config:
        from_attributes = True
        
class PerfilCreate(BaseModel):
    idade: int
    endereco: str
    nome_mae: str
    nome_pai: str
    numero_emergencia: int

class Estudante(BaseModel):
    id: int
    nome: str
    perfil: Optional[Perfil] = None
    
    class Config:
        from_attributes = True
    
class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate

class Professor(BaseModel):
    id: int
    nome: str
    materias: str
    email: str
    numero: int

    class Config:
        from_attributes = True

class ProfessorCreate(BaseModel):
    nome: str
    materias: str
    email: str
    numero: int
    
class Funcionario(BaseModel):
    id: int
    nome: str
    servico: str
    email: str
    numero: int

    class Config:
        from_attributes=True

class FuncionarioCreate(BaseModel):
    nome: str
    servico: str
    email: str
    numero: int
