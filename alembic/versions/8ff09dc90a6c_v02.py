"""V02

Revision ID: 8ff09dc90a6c
Revises: 4d297ed8430f
Create Date: 2024-03-24 16:27:50.914206

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from infra.configs.connection import DBConnectionHandler
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = '8ff09dc90a6c'
down_revision: Union[str, None] = '4d297ed8430f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    
    with engine.connect() as connection:
        connection.execute(
            text(
                '''CREATE TABLE IF NOT EXISTS atores (
                id BIGINT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(50) NOT NULL,
                titulo_filme VARCHAR(50) NOT NULL,
                PRIMARY KEY(id),
                FOREIGN KEY (titulo_filme) REFERENCES filmes(titulo)
                );''')
        )


def downgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text('''
                DROP TABLE IF EXISTS atores;
            ''')
        )
