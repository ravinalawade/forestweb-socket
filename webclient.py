from websocket import create_connection
# ws = create_connection("ws://forestwebsocket.herokuapp.com/test")
ws = create_connection("ws://127.0.0.1:8000/test")
# print("Sending 'Hello, World'...")
# ws.send("send task")
# print("Sent")
# print("Receiving...")
result =  ws.recv()
print(result)
ws.close()
# import asyncio
# import websockets

# uri = "ws://127.0.0.1:8000/test"
# websockets.connect(uri)

# async def hello():
#     uri = "ws://127.0.0.1:8000/test"
#     async with websockets.connect(uri) as web:
#         await web.send("send task")
#         print(await web.recv())

# asyncio.get_event_loop().run_until_complete(hello())