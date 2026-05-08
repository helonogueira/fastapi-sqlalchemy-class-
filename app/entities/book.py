from pydantic import BaseModel, Field
from typing import Optional, List

class Book(BaseModel):
    """
    Entidade Book usando Pydantic.
    Representa um livro no domínio da aplicação.

    Attributes:
        id (Optional[int]): Identificador único do livro, gerado pelo banco.
        title (str): Título do livro.
        isbn (Optional[str]): Código ISBN do livro, entre 10 e 17 caracteres.
        authors (List[Author]): Lista de autores associados ao livro.
    """
    id: Optional[int] = Field(None, description="ID do livro", example=1)
    title: str = Field(..., min_length=1, max_length=500, description="Título do livro", example="Clean Code")
    isbn: Optional[str] = Field(None, min_length=10, max_length=17, description="ISBN do livro", example="978-0132350884")
    authors: List['Author'] = Field(default_factory=list, description="Lista de autores do livro")

    class Config:
        from_attributes = True

    def __str__(self):
        """
        Retorna uma representação legível do livro.

        Returns:
            str: String no formato 'Book: título'.
        """
        return f"Book: {self.title}"

from .author import Author
Book.model_rebuild()