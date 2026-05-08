from sqlalchemy.orm import Session
from typing import TypeVar, Type, Generic

T = TypeVar('T')

class BaseRepository(Generic[T]):
    """
    Repositório base com operações CRUD genéricas.
    Utiliza Generic[T] para ser reutilizável com qualquer modelo SQLAlchemy.

    Attributes:
        session (Session): Sessão ativa do SQLAlchemy.
        model (Type[T]): Classe do modelo associado ao repositório.
    """

    def __init__(self, session: Session, model: Type[T]):
        """
        Inicializa o repositório com uma sessão e um modelo.

        Args:
            session (Session): Sessão ativa do SQLAlchemy.
            model (Type[T]): Classe do modelo SQLAlchemy.
        """
        self.session = session
        self.model = model

    def get_all(self) -> list[T]:
        """
        Retorna todas as entidades do banco de dados.

        Returns:
            list[T]: Lista com todas as entidades encontradas.
        """
        return self.session.query(self.model).all()

    def get_by_id(self, id: int) -> T | None:
        """
        Busca uma entidade pelo ID.

        Args:
            id (int): O ID da entidade a ser buscada.

        Returns:
            T | None: A entidade encontrada ou None se não existir.
        """
        return self.session.query(self.model).filter(self.model.id == id).first()

    def add(self, entity: T) -> T:
        """
        Adiciona uma nova entidade ao banco de dados.

        Args:
            entity (T): A entidade a ser adicionada.

        Returns:
            T: A entidade adicionada com o ID gerado pelo banco.
        """
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def update(self, entity: T) -> T:
        """
        Atualiza uma entidade existente no banco de dados.

        Args:
            entity (T): A entidade com os dados atualizados.

        Returns:
            T: A entidade atualizada.
        """
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, id: int) -> T | None:
        """
        Remove uma entidade do banco de dados pelo ID.

        Args:
            id (int): O ID da entidade a ser removida.

        Returns:
            T | None: A entidade removida ou None se não encontrada.
        """
        entity = self.get_by_id(id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
            return entity