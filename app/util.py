import requests
r = requests.get('https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/ATP', timeout=1)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.json())