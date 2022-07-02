import requests

EBI_API_URL = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/'


def get_ebi_compound(compound):
    """Return list prepared for model compounds from ebi.ac.uk API"""
    api_resp = requests.get(f'{EBI_API_URL}{compound}', timeout=1)
    api_compound_dict = api_resp.json()
    compound_models = []
    for compound, compound_list in api_compound_dict.items():
        for item in compound_list:
            compound_model = dict()
            compound_model['compound'] = compound
            compound_model['name'] = item['name']
            compound_model['formula'] = item['formula']
            compound_model['inchi'] = item['inchi']
            compound_model['inchi_key'] = item['inchi_key']
            compound_model['smiles'] = item['smiles']
            compound_model['cross_links_count'] = len(item['cross_links'])

            compound_models.append(compound_model)
    return api_resp.status_code, compound_models


