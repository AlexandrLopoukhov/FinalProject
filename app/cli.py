import click
from controllers.user_controller import api_get
from services.user_service import post
from config import app

@click.command()
# @click.option('--count', default=1, help='Number of greetings.')
@click.option('--action')
@click.option('--user')
def hello(action, user):
    """Simple program that greets NAME for a total of COUNT times."""
    if action == 'load':
        post({'id': 2, 'handle': 'nanana'})

    if action == 'get':
        click.echo(api_get())

if __name__ == '__main__':
    with app.app_context():
        hello()