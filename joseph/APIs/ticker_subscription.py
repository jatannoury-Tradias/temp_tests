import asyncio
import websockets
import json
import config

MY_TOKEN = config.UAT_TOKEN
ENVIRONMENT = 'otcapp-UAT'
PROTOCOL = 'wss'

URI = f"{PROTOCOL}://{ENVIRONMENT}.tradias.de/otc/ws"

headers = {
    "x-token-id": MY_TOKEN
}


async def get_prices(instrument: str) -> None:

    async with websockets.connect(uri=URI, extra_headers=headers) as websocket:
        await websocket.send(json.dumps({
            "type": "subscribe",
            "channelname": "prices",
            "instrument": instrument,
            "heartbeat": True
        }))
        while True:
            message = json.loads(await websocket.recv())
            if "levels" in message:
                return message


asyncio.run(get_prices(instrument='BTCEUR'))

