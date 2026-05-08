from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base # Classe base do SQLAIchemy para todos os models

# Tabela de associação ja criada, nao precisa ser criada novamente 

class BookModel(Base):
    __tablename__ = "books"  # Nome da tabela no banco

    # Column define cada coluna da tabela  
    id = Column(Integer, primary_key=True, index=True)  # Chave primária
    title = Column(String, index=True)                   # titulo
    isbn = Column(String, unique=True, index=True)     # ISBN (sinopse)
    loans = relationship("LoanModel", back_populates="book")

   
    # relationship cria o relacionamento entre tabelas
    authors = relationship( # authors: relacionamento com autores
        "AuthorModel",
        secondary="author_book_association", # secondary: nome da tabela de associação
        back_populates="books" # conecta o relacionamento reverso 
    )

    def __repr__(self):
        return f"<BookModel(id={self.id}, name='{self.title}', email='{self.isbn}')>"