import os
import pymysql
import click
from flask import current_app, g
from flask.cli import with_appcontext
from instance.config import Config

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
                host='localhost',
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                db='crimemap'
                )
        # return rows as dicts
    return g.db

def close_db(e=None):
    print(e)
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('db/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""

    init_db()
    click.echo('Initialized the database')

# Register above commands with the application
def init_app(app):
    # call close_db when cleaning up after returning a response
    app.teardown_appcontext(close_db)
    # add a new command that can be called with flask command
    app.cli.add_command(init_db_command)
