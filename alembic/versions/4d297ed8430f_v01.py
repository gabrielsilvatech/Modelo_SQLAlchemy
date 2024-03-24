"""V01

Revision ID: 4d297ed8430f
Revises: 
Create Date: 2024-03-24 15:28:29.065519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from infra.configs.connection import DBConnectionHandler
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision: str = '4d297ed8430f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    
    with engine.connect() as connection:
        connection.execute(
            text('''
                CREATE TABLE IF NOT EXISTS filmes (
                titulo VARCHAR(50) NOT NULL,
                genero VARCHAR(30) NOT NULL,
                ano INT NOT NULL,
                PRIMARY KEY(titulo));
            ''')
        )


def downgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()

    with engine.connect() as connection:
        connection.execute(
            text('''
                DROP TABLE IF EXISTS filmes;
            ''')
        )
