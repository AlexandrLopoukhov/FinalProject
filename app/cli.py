import click
from services.compound_service import post, get
from config import app
from util import get_ebi_compound, CliAction
import pandas as pd

from tabulate import tabulate


@click.command()
@click.option('--action', help='Number of greetings.', required=True)
@click.option('--compound', help='Name of compound for load action', required=False)
def cli_action(action, compound):
    supported_actions = [action.value for action in CliAction]
    if action not in supported_actions:
        raise Exception(f'Not supported action. Supported - {supported_actions}')

    if action == CliAction.load.value:
        status, compound_list = get_ebi_compound(compound)
        for compound in compound_list:
            post(compound)

    if action == CliAction.get.value:
        compounds = get()
        compounds_formated = [compound.as_formated_dict(field_width=10) for compound in compounds]
        compounds_df = pd.DataFrame.from_dict(compounds_formated)
        click.echo(compounds_df)


if __name__ == '__main__':
    with app.app_context():
        cli_action()
