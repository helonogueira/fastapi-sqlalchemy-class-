from pydantic import BaseModel, Field
from typing import List

class CreateBookRequest(BaseModel):
    """
    DTO para requisição de criação de livro.
    Contém os dados necessários para criar um novo livro.
    """
    title: str = Field(..., min_length=1, max_length=255, description="Título do livro", example="Clean Code")
    isbn: str = Field(..., description="ISBN do livro", example="978-0132350884")

class UpdateBookRequest(BaseModel):
    """
    DTO para requisição de atualização de livro.
    Contém os dados que podem ser atualizados em um livro.
    """
    title: str = Field(..., min_length=1, max_length=255, description="Novo título do livro", example="Clean Code")
    isbn: str = Field(..., description="Novo ISBN do livro", example="978-0132350884")

class AuthorSummary(BaseModel):
    """
    DTO com resumo das informações de um autor.
    Usado para evitar referências circulares na resposta de livros.

    Attributes:
        id (int): Identificador único do autor.
        name (str): Nome completo do autor.
        email (str): Email do autor.
    """
    id: int = Field(..., description="ID único do autor", example=1)
    name: str = Field(..., description="Nome completo do autor", example="Robert C. Martin")
    email: str = Field(..., description="Email do autor", example="robert@example.com")

    class Config:
        from_attributes = True

class BookResponse(BaseModel):
    """
    DTO de resposta para operações com livros.
    Contém todas as informações do livro incluindo seus autores.

    Attributes:
        id (int): Identificador único do livro.
        title (str): Título do livro.
        isbn (str): Código ISBN do livro.
        authors (List[AuthorSummary]): Lista resumida dos autores do livro.
    """
    id: int = Field(..., description="ID único do livro", example=1)
    title: str = Field(..., description="Título do livro", example="Clean Code")
    isbn: str = Field(..., description="ISBN do livro", example="978-0132350884")
    authors: List[AuthorSummary] = Field(default_factory=list, description="Lista de autores do livro")

    class Config:
        from_attributes = True