import click
from services.compound_service import post, get
from config import app
from util import get_ebi_compound

from tabulate import tabulate


@click.command()
@click.option('--action')
@click.option('--compound')
def hello(action, compound):
    if action == 'load':
        status, compound_list = get_ebi_compound(compound)
        for compound in compound_list:
            post(compound)

    if action == 'get':
        compounds = get()
        for compound in compounds:
            click.echo(compound.as_dict())


if __name__ == '__main__':
    with app.app_context():
        hello()