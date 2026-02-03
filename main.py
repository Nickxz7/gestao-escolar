from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session 
import models, schema
from database import engine, SessionLocal
from typing import List 
from sqlalchemy.orm import joinedload


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes/', response_model=schema.Estudante)
def criar_estudante(
        estudante: schema.EstudanteCreate,
        db: Session = Depends(get_db)
    ):
    db_estudante=models.Estudante(
        nome = estudante.nome,
        perfil = models.Perfil(**estudante.perfil.dict())
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante

@app.get('/estudante/', response_model=List[schema.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).all()
    return estudantes

@app.post('/professor/', response_model = schema.Professor)
def criar_professor(
        professor: schema.ProfessorCreate,
        db: Session = Depends(get_db)
    ):
    db_professor=models.Professor(
        **professor.dict()
    )
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

@app.get('/professor/', response_model = List[schema.Professor])
def Listar_professores(db: Session = Depends(get_db)):
    return db.query(models.Professor).all()

@app.post('/funcionario/', response_model = schema.Funcionario)
def criar_funcionario(
        funcionario: schema.FuncionarioCreate,
        db: Session = Depends(get_db)
    ):
    db_funcionario=models.Funcionario(
        **funcionario.dict()
    )
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario

@app.get('/funcionario/', response_model=List[schema.Funcionario])
def Listar_funcionario(db: Session = Depends(get_db)):
    return db.query(models.Funcionario).all()
        

