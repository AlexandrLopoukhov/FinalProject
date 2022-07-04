from enum import Enum
import click
from services.compound_service import post, get
from config import app
from api_request import get_ebi_compound, DEFAULT_COMPOUNDS_TO_LOAD
import pandas as pd


class CliAction(Enum):
    """Holds supported CLI actions"""
    load = 'load'
    get = 'get'
    load_default = 'load_default'


@click.command()
@click.option('--action', help='Number of greetings.', required=True)
@click.option('--compound', help='Name of compound for load action', required=False)
def cli_action(action, compound):
    """Dispatcher of CLI commands"""
    supported_actions = [action.value for action in CliAction]
    if action not in supported_actions:
        raise Exception(f'Not supported action. Supported - {supported_actions}')

    if action == CliAction.load.value:
        status, compound_list = get_ebi_compound(compound)
        for compound in compound_list:
            post(compound)

    if action == CliAction.load_default.value:
        for compound in DEFAULT_COMPOUNDS_TO_LOAD:
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