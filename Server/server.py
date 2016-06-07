#!/usr/bin/env python

# Modified from https://websockets.readthedocs.io/en/stable/intro.html
# Pushes the current utc time to every second on port 12345

# asyncio and websockets are used to open the connection and send and receive things
import asyncio
import websockets

# datetime is a package that provides a lot of resources pertaining to time
# This program uses it to send a UTC timestamp through the socket to the webpage
import datetime

# This is the section of code that actually sends the message
# I don't completely understand how this works, but my plan should still work -- I want to send data every tenth of a second or so
async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z' # Put the message together
        await websocket.send(now) #Send the message
        await asyncio.sleep(0.01) #Wait 0.01 seconds

start_server = websockets.serve(time, '127.0.0.1', 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()