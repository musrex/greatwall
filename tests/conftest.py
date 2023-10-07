import os
import tempfile

import pytest
from main import create_app
from main.db import get_db, init_db

'''This line of code reads the data.sql file in this same directory '/tests/'
as bytes ('rb') and then decodes it to a string using UTF-8 encoding and stores
it in the '_data_sql' variable. We will use the '_data_sql' variable later to
test our app.
'''
with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    '''This fixture creates and configures an instance of our app for testing.
    - tempfile.mkstemp() creates a temporary file and returns a descriptor('db_fd')
    and the files path('db_path'). The path is used as a temporary database 
    location for testing.
    - create_app() constructs and configures an instance of our app set to
    'TESTING' and using the DATABASE path created by tempfile.mkstemp()
    - within the app_context, we run init_db and pass our _data_sql
    through get_db(). yield pauses the fixture while tests run, and then
    os.close() and os.unlink() clean up and close the tempfile.
    '''
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    '''This fixture creates a test client for our app. test_client() allows
    us to test the app without running a server.
    '''
    return app.test_client()

@pytest.fixture
def runner(app):
    '''This fixture is similare to the 'client' fixture. test_cli_runner()
    lets us run the Click commands registed with our app, i.e. init-db.
    '''
    return app.test_cli_runner()

class AuthActions(object):
    '''This class helps us send POST request to the 'login' view so that we can
    test features that require a user login.
    '''
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
                '/auth/login',
                data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
    '''With this fixture, we can call auth.login() in a test to login in as the test
    user, which was provided in the data.sql file
    '''
    return AuthActions(client)
