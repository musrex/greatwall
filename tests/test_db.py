import sqlite3

import pytest
from main.db import get_db

def test_get_close_db(app):
    '''This function verifies 2 things:
        1) That the get_db() function returns the same database connection
        within the same application context.
        2) The database connection gets closed once the context ends.
        Parameters: app, an instance of the Flask app configured for testing
    '''
    with app.app_context():
        db = get_db()
        assert db is get_db()
 
    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)

def test_init_db_command(runner, monkeypatch):
    '''This function tests whether the command-line command 'init-db'
    is being properly initialized. The Recorder object simply exists so
    that we can make sure our fake_init_db is called. The monkeypatch.setattr()
    method is used to replace our real init_db with the fake one, to avoid 
    messing with our real database.
    '''
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('main.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
