from fastapi import APIRouter, Depends
from repositories.author_repository import AuthorRepository
from database.database import get_db
from sqlalchemy.orm import Session
from dtos.author_dto import AuthorResponse
from use_cases.authors.get_all_authors_use_case.get_all_authors_use_case import GetAllAuthorsUseCase
from pathlib import Path

router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> GetAllAuthorsUseCase:
    author_repository = AuthorRepository(db)
    return GetAllAuthorsUseCase(author_repository)

@router.get("/authors", response_model=list[AuthorResponse],
    description=Path("app/docs/get_all_authors.md").read_text(),
    summary="Listar Autores", tags=["Authors"])
def get_all_authors(use_case: GetAllAuthorsUseCase = Depends(get_use_case)):
    return use_case.execute()