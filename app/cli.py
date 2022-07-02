import click
from services.compound_service import post, get
from config import app
from tabulate import tabulate


@click.command()
@click.option('--action')
@click.option('--user')
def hello(action, user):
    if action == 'load':
        post({'id': 2, 'handle': 'nanana'})

    if action == 'get':
        users = get()
        for user in users:
            click.echo(user.as_dict())


if __name__ == '__main__':
    with app.app_context():
        hello()