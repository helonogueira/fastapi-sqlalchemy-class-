from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Loan(BaseModel):
    """
    Entidade Loan usando Pydantic.
    Representa um empréstimo de livro no domínio da aplicação.

    Attributes:
        id (Optional[int]): Identificador único do empréstimo, gerado pelo banco.
        book_id (int): ID do livro emprestado.
        user_name (str): Nome do usuário que realizou o empréstimo.
        loan_date (date): Data em que o empréstimo foi realizado.
        return_date (Optional[date]): Data prevista ou efetiva de devolução.
        returned (bool): Indica se o livro já foi devolvido. Padrão False.
    """
    id: Optional[int] = Field(None, description="ID do empréstimo", example=1)
    book_id: int = Field(..., description="ID do livro emprestado", example=3)
    user_name: str = Field(..., min_length=1, max_length=255, description="Nome do usuário", example="Maria Souza")
    loan_date: date = Field(..., description="Data do empréstimo", example="2025-01-15")
    return_date: Optional[date] = Field(None, description="Data de devolução", example="2025-01-30")
    returned: bool = Field(False, description="Indica se o livro foi devolvido", example=False)

    class Config:
        from_attributes = True

    def __str__(self):
        """
        Retorna uma representação legível do empréstimo.

        Returns:
            str: String com nome do usuário, ID do livro e status do empréstimo.
        """
        status = "Devolvido" if self.returned else "Em aberto"
        return f"Loan: {self.user_name} - Book ID: {self.book_id} ({status})"