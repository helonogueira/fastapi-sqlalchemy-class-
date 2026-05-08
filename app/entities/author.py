from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

class Author(BaseModel):
    """
    Entidade Author usando Pydantic.
    Representa um autor no domínio da aplicação.

    Attributes:
        id (Optional[int]): Identificador único do autor, gerado pelo banco.
        name (str): Nome completo do autor.
        email (EmailStr): Email válido do autor.
        books (List[Book]): Lista de livros associados ao autor.
    """
    id: Optional[int] = Field(None, description="ID do autor", example=1)
    name: str = Field(..., min_length=1, max_length=255, description="Nome do autor", example="João Silva")
    email: EmailStr = Field(..., description="Email do autor", example="joao.silva@example.com")
    books: List['Book'] = Field(default_factory=list, description="Lista de livros do autor")

    class Config:
        from_attributes = True

    def __str__(self):
        """
        Retorna uma representação legível do autor.

        Returns:
            str: String no formato 'Author: nome (email)'.
        """
        return f"Author: {self.name} ({self.email})"

from .book import Book
Author.model_rebuild()