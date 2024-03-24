from infra.entities.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound

class FilmesRepository:
    
    def __init__(self, ConnectionHandler) -> None:
        self.__connectionHandler = ConnectionHandler
    
    def select(self):
        with self.__connectionHandler() as db:
            try:
                data = db.session.query(Filmes).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_drama_filmes(self):
        with self.__connectionHandler() as db:
            try:
                data = db.session.query(Filmes).filter(Filmes.genero=="Drama").one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, titulo, genero, ano):
        with self.__connectionHandler() as db:
            try:
                data_isert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_isert)
                db.session.commit()
                return data_isert
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, titulo):
        with self.__connectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, titulo, ano):
        with self.__connectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).update({ "ano": ano })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception