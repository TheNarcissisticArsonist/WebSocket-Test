#!/usr/bin/env python

# Modified from https://websockets.readthedocs.io/en/stable/intro.html
# Pushes the current utc time to every second on port 12345

import asyncio
import datetime
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(1)

start_server = websockets.serve(time, '127.0.0.1', 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()