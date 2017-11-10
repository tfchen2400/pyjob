import asyncio

import datetime
import random

import websockets

connected = set()


async def handler(websocket, path):
    global connected
    # Register.
    connected.add(websocket)
    try:
        # Implement logic here.
        await asyncio.wait([ws.send("Hello!" + str(websocket)) for ws in connected])
        while True:
            await asyncio.sleep(10)
    finally:
        # Unregister.
        connected.remove(websocket)


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message + "12233")


async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)


start_server = websockets.serve(handler, '0.0.0.0', 9001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
