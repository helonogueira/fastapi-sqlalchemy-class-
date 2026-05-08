from pydantic import BaseModel, EmailStr, Field
from typing import List

class CreateAuthorRequest(BaseModel):
    """
    DTO para requisição de criação de autor.
    Contém os dados necessários para criar um novo autor.
    """
    name: str = Field(..., min_length=1, max_length=255, description="Nome completo do autor", example="João Silva")
    email: EmailStr = Field(..., description="Email válido do autor", example="joao.silva@example.com")

class UpdateAuthorRequest(BaseModel):
    """
    DTO para requisição de atualização de autor.
    Contém os dados que podem ser atualizados em um autor.
    """
    name: str = Field(..., min_length=1, max_length=255, description="Novo nome completo do autor", example="João Silva")
    email: EmailStr = Field(..., description="Novo email válido do autor", example="joao.silva@example.com")

class BookSummary(BaseModel):
    """
    DTO com resumo das informações de um livro.
    Usado para evitar referências circulares na resposta de autores.

    Attributes:
        id (int): Identificador único do livro.
        title (str): Título do livro.
        isbn (str): Código ISBN do livro.
    """
    id: int = Field(..., description="ID único do livro", example=1)
    title: str = Field(..., description="Título do livro", example="Clean Code")
    isbn: str = Field(..., description="ISBN do livro", example="978-0132350884")

    class Config:
        from_attributes = True

class AuthorResponse(BaseModel):
    """
    DTO de resposta para operações com autores.
    Contém todas as informações do autor incluindo seus livros.

    Attributes:
        id (int): Identificador único do autor.
        name (str): Nome completo do autor.
        email (str): Email do autor.
        books (List[BookSummary]): Lista resumida dos livros do autor.
    """
    id: int = Field(..., description="ID único do autor", example=1)
    name: str = Field(..., description="Nome completo do autor", example="João Silva")
    email: str = Field(..., description="Email do autor", example="joao.silva@example.com")
    books: List[BookSummary] = Field(default_factory=list, description="Lista de livros escritos pelo autor")

    class Config:
        from_attributes = True