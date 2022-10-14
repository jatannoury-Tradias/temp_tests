import asyncio
import websockets
import json
import config
from joseph.tests.variables import *
import os
MY_TOKEN = config.UAT_TOKEN
ENVIRONMENT = 'otcapp-UAT'
PROTOCOL = 'wss'

URI = f"{PROTOCOL}://{ENVIRONMENT}.tradias.de/otc/ws"

headers = {
    "x-token-id": MY_TOKEN
}


async def getInboundChannel(instrument: str) -> None:

    async with websockets.connect(uri=URI, extra_headers=headers) as websocket:
        await websocket.send(json.dumps({
            "type": "subscribe",
            "channelname": "prices",
            "instrument": instrument,
            "heartbeat": True
        }))
        data=[]
        while True:
            message = json.loads(await websocket.recv())
            data.append(message)
            if len(data)==3:
                return data[-1][instrument]

async def get_price_precision(instrument):
        return currencyMaster[instrument[:len(instrument)-3]]["Smallest Acceptable Unit"]
# asyncio.run(get_price_precision("B2C2","BTCEUR"))




