import asyncio
from joseph.tests.variables import *
import websockets
import json

import config

MY_TOKEN = config.UAT_TOKEN2
ENVIRONMENT = 'otcapp-uat'
PROTOCOL = 'wss'


URI = f"{PROTOCOL}://{ENVIRONMENT}.tradias.de/otc/ws"

headers = {
    "x-token-id": MY_TOKEN
}

order_channel_subscription = {
    "type": "subscribe",
    "channelname": "orders"
}




async def make_orders(orders_to_be_sent: list[dict],correct_body=False) -> None:
    async with websockets.connect(uri=URI, extra_headers=headers) as websocket:
        await websocket.send(json.dumps(order_channel_subscription))
        for order in orders_to_be_sent:
            asyncio.create_task(websocket.send(json.dumps(order)))
        data=[]
        while True:
            message = json.loads(await websocket.recv())
            if "event" in message:
                data.append(message)
            elif ("message" in message and message['message']!="success") and ("message" in message and message['message']!="Websocket Connected"):
                return message
            if correct_body==True and len(data)==2:
                return data
            if correct_body==False and len(data)==1:
                return data[0]

