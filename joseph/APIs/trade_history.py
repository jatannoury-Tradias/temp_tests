import requests
import json
import config
MY_TOKEN = config.UAT_TOKEN2
ENVIRONMENT = 'otcapp-uat'
PROTOCOL = 'https'
VERSION = 'v2'  # v1 documentation + examples are available on APIs

HISTORY_API_URL = f"{PROTOCOL}://{ENVIRONMENT}.tradias.de/otc/api/{VERSION}/history/report"

rest_api_header = {
    "Authorization": "Bearer " + MY_TOKEN
}

wrong_rest_api_header = {
    "Authorization": "Bearer " + config.WRONG_TOKEN
}


def get_history_response(filter_body: dict = None,wrong_token=False):

    if not filter_body:
        filter_body = dict()

    if(not wrong_token):
        return requests.post(url=HISTORY_API_URL,
                             headers=rest_api_header,
                             json=filter_body).json()
    return requests.post(url=HISTORY_API_URL,
                         headers=wrong_rest_api_header,
                         json=filter_body).json()


def print_and_show(history_response: dict) -> None:
    history_response['trades'] = history_response['trades'][0]  # show the first trade


# Get all trades:
