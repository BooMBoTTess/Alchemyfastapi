from typing import Generator
import config
import pytest
from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import Session
from src.uapp import app


@pytest.fixture(scope='session')
def db_engine():
    """Creates a test database and yields a database engine"""

    engine = create_engine(
        config.DATABASE_URL,
    )
    yield engine

@pytest.fixture(scope='function')
def db_session(db_engine):
    """Creates a connection to the test database and handles cleanup"""
    connection = db_engine.connect()
    # Begin a non-ORM transaction
    database_session = Session(bind=connection, expire_on_commit=False)
    yield database_session
    database_session.rollback()
    connection.close()


@pytest.fixture(scope='function')
def client(db_session) -> Generator[TestClient, None, None]:
    """
    Надо настроить чтобы он был соеденен с игрушечной базой данных наверно
    """

    with TestClient(app) as test_client:
        yield test_client



def test_read_exist_departments(client):

    response = client.get('/info')
    assert response.status_code == 202

def test_read_departments(client):
    for i in range(3):
        response = client.get(f'/info/{i}')
        assert response.status_code == 200
    response = client.get(f'/info/54')
    assert response.status_code == 204
