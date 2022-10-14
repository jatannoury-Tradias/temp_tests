import requests
import config
import Test_objects
headers = {'Accept': 'application/json',  'Authorization': f'Bearer {config.UAT_TOKEN3}'}
wrong_headers = {'Accept': 'application/json',  'Authorization': f'Bearer {Test_objects.wrong_headers}'}
ENVIRONMENT = 'otcapp-uat'
PROTOCOL = 'https'
def getRiskFigures(wrong_header=False):
    response= requests.post(f'{PROTOCOL}://{ENVIRONMENT}.tradias.de/otc/api/v1/riskfigures/report', headers = headers)
    if wrong_header==True:
        response = requests.post(f'{PROTOCOL}://{ENVIRONMENT}.tradias.de/otc/api/v1/riskfigures/report',headers=wrong_headers)
    return response

getRiskFigures()
