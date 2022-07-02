import click
from services.compound_service import post, get
from config import app
from util import get_ebi_compound
import pandas as pd

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
        l = [i.as_cut_formated(10) for i in compounds]
        df = pd.DataFrame.from_dict(l)
        # for compound in compounds: tablefmt="fancy_grid" maxcolwidths
        #     click.echo(compound.as_dict())
        click.echo(df)


if __name__ == '__main__':
    with app.app_context():
        hello()