import pytest
from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import create_engine

from src.uapp import app
@pytest.fixture(scope='session')
def db_engine():
    """Creates a test database and yields a database engine"""

    engine = create_engine(
        SQLALCHEMY_TEST_DATABASE_URL,
        connect_args={
            'check_same_thread': False
        }
    )

    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope='function')
def db_session(db_engine):
    """Creates a connection to the test database and handles cleanup"""

    connection = db_engine.connect()

    # Begin a non-ORM transaction
    _ = connection.begin()

    database_session = Session(bind=connection, expire_on_commit=False)

    yield database_session

    database_session.rollback()
    connection.close()


@pytest.fixture(scope='function')
def client(db_session) -> Generator[TestClient, None, None]:
    """
    Overrides the normal database access with test database,
    and yields a configured test client
    """

    app.dependency_overrides[get_db] = lambda: db_session

    with TestClient(app) as test_client:
        yield test_client

def test_read_departments():
    response = client.get('/info')
    assert response.status_code == 202

def test_read_exist_departments():
    for i in range(0,4):
        response = client.get('/info/0')
        assert response.status_code == 202


test_read_departments()
test_read_exist_departments()
