from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base # Classe base do SQLAIchemy para todos os models

# Tabela de associação para o relacionamento many-to-many
author_book_association = Table(
    'author_book_association',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True)
)

class AuthorModel(Base):
    __tablename__ = "authors"  # Nome da tabela no banco

    # Column define cada coluna da tabela  
    id = Column(Integer, primary_key=True, index=True)  # Chave primária
    name = Column(String, index=True)                   # Nome do autor
    email = Column(String, unique=True, index=True)     # Email único

    # Relacionamento many-to-many com livros
    # relationship cria o relacionamento entre tabelas
    books = relationship(
        "BookModel",                      # Classe relacionada
        secondary=author_book_association, # Tabela de associação, tabela extra para o relacionamento many-to-many
        back_populates="authors"          # Relacionamento reverso
    )

    def __repr__(self):
        return f"<AuthorModel(id={self.id}, name='{self.name}', email='{self.email}')>"