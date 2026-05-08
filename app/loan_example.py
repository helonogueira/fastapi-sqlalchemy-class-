from datetime import date
from database.database import SessionLocal, Base, engine
from models.author_model import AuthorModel
from models.book_model import BookModel
from models.loan_model import LoanModel
from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository
from repositories.loan_repository import LoanRepository

# Garante que as tabelas existem no banco
Base.metadata.create_all(bind=engine)

def main():
    session = SessionLocal()

    try:
        # Limpar dados existentes
        session.query(LoanModel).delete()
        session.query(BookModel).delete()
        session.query(AuthorModel).delete()
        session.commit()

        # Instanciar repositórios
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        loan_repo = LoanRepository(session)

        # Criar autor e livro
        author = AuthorModel(name="Machado de Assis", email="machado@email.com")
        author = author_repo.add(author)
        print(f"Autor criado: {author}")

        book = BookModel(title="Dom Casmurro", isbn="978-8525406958")
        book = book_repo.add(book)
        print(f"Livro criado: {book}")

        # Criar empréstimo
        loan = LoanModel(
            book_id=book.id,
            user_name="Ana Silva",
            loan_date=date.today(),
            return_date=None,
            returned=False
        )
        loan = loan_repo.add(loan)
        print(f"Empréstimo criado: {loan}")

        # Buscar empréstimos ativos
        active_loans = loan_repo.get_active_loans()
        print(f"\nEmpréstimos ativos: {len(active_loans)}")
        for l in active_loans:
            print(f"  - {l.user_name} pegou '{l.book.title}' em {l.loan_date}")

        # Marcar como devolvido
        loan.returned = True
        loan.return_date = date.today()
        loan_repo.update(loan)
        print(f"\nLivro devolvido por {loan.user_name}!")

        # Confirma que não há mais empréstimos ativos
        active_loans = loan_repo.get_active_loans()
        print(f"Empréstimos ativos após devolução: {len(active_loans)}")

    finally:
        session.close()

if __name__ == "__main__":
    main()