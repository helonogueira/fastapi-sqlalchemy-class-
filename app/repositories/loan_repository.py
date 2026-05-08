from sqlalchemy.orm import Session
from models.loan_model import LoanModel
from repositories.base_repository import BaseRepository

class LoanRepository(BaseRepository[LoanModel]):
    """
    Repositório de empréstimos com operações específicas além do CRUD básico.
    """

    def __init__(self, session: Session):
        """
        Inicializa o repositório com a sessão do banco de dados.

        Args:
            session (Session): Sessão ativa do SQLAlchemy.
        """
        super().__init__(session, LoanModel)

    def get_by_user(self, user_name: str) -> list[LoanModel]:
        """
        Busca empréstimos pelo nome do usuário usando busca parcial (case-insensitive).

        Args:
            user_name (str): Trecho do nome do usuário a ser buscado.

        Returns:
            list[LoanModel]: Lista de empréstimos associados ao usuário.
        """
        return self.session.query(LoanModel).filter(LoanModel.user_name.ilike(f"%{user_name}%")).all()

    def get_active_loans(self) -> list[LoanModel]:
        """
        Retorna todos os empréstimos ainda não devolvidos.

        Returns:
            list[LoanModel]: Lista de empréstimos ativos (não devolvidos).
        """
        return self.session.query(LoanModel).filter(LoanModel.returned == False).all()

    def get_by_book(self, book_id: int) -> list[LoanModel]:
        """
        Busca todos os empréstimos de um livro específico.

        Args:
            book_id (int): ID do livro a ser buscado.

        Returns:
            list[LoanModel]: Lista de empréstimos do livro informado.
        """
        return self.session.query(LoanModel).filter(LoanModel.book_id == book_id).all()