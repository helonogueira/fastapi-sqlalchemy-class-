from sqlalchemy.orm import Session
from models.book_model import BookModel
from repositories.base_repository import BaseRepository

class BookRepository(BaseRepository[BookModel]):
    """
    Repositório de livros com operações específicas além do CRUD básico.
    """

    def __init__(self, session: Session):
        """
        Inicializa o repositório com a sessão do banco de dados.

        Args:
            session (Session): Sessão ativa do SQLAlchemy.
        """
        super().__init__(session, BookModel)

    def get_by_title(self, title: str) -> list[BookModel]:
        """
        Busca livros pelo título usando busca parcial (case-insensitive).

        Args:
            title (str): Trecho do título a ser buscado.

        Returns:
            list[BookModel]: Lista de livros cujo título contém o trecho informado.
        """
        return self.session.query(BookModel).filter(BookModel.title.ilike(f"%{title}%")).all()

    def get_by_isbn(self, isbn: str) -> BookModel | None:
        """
        Busca um livro pelo ISBN (busca exata).

        Args:
            isbn (str): O ISBN do livro a ser buscado.

        Returns:
            BookModel | None: O livro encontrado ou None se não existir.
        """
        return self.session.query(BookModel).filter(BookModel.isbn == isbn).first()

    def get_books_with_authors(self) -> list[BookModel]:
        """
        Retorna livros com as informações dos autores carregadas via join.

        Returns:
            list[BookModel]: Lista de livros que possuem autores associados.
        """
        return self.session.query(BookModel).join(BookModel.authors).all()