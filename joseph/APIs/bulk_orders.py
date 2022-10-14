import io
import json
import requests
import config
from joseph.tests.variables import  *
MY_TOKEN =config.UAT_TOKEN
ENVIRONMENT = 'otcapp-UAT'
PROTOCOL = 'https'


URI = f"{PROTOCOL}://{ENVIRONMENT}.tradias.de/otc/api/v1/order/bulk"


headers = {
    "Authorization": f"Bearer {MY_TOKEN}"
}




def send_bulk_order(custom_order="",custom_order_state=False):
    # When using from a locally stored file, replace the following line using
    # with open(file_path, 'rb') as f:
    if custom_order_state==True:
        with custom_order as f:
            response = requests.post(URI, headers=headers, files={"bulk-orders-file": f})
            return response.json()
    with my_bulk_order_in_memory_file as f:
        response = requests.post(URI, headers=headers, files={"bulk-orders-file": f})
    return response.json()


def get_bulk_order(bulk_order_id):
    full_path = URI + "/" + bulk_order_id
    r = requests.get(full_path, headers=headers)
    return r.json()


