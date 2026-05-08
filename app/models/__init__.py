from .author_model import AuthorModel, author_book_association
from .book_model import BookModel
from .loan_model import LoanModel

__all__ = ["AuthorModel", "BookModel", "LoanModel", "author_book_association"]

'''
Sempre use back_populates nos dois lados do relacionamento
O nome da tabela de associação deve ser igual nos dois models
O SQLAlchemy não valida tipos automaticamente: use Pydantic nas entidades para isso
O método __repr__ ajuda no debug e nos prints
'''
