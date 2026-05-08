from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class LoanModel(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))  # Chave estrangeira para books
    user_name = Column(String, index=True)
    loan_date = Column(Date)
    return_date = Column(Date, nullable=True)  # Opcional
    returned = Column(Boolean, default=False)

    # Relacionamento com BookModel
    book = relationship("BookModel", back_populates="loans")

    def __repr__(self):
        return f"<LoanModel(id={self.id}, user='{self.user_name}', book_id={self.book_id}, returned={self.returned})>"