# /// script
# dependencies = ["aiocoap"]
# ///

import asyncio
import random
from aiocoap import resource, Context, Message
from aiocoap.numbers.codes import Code

class SensorResource(resource.Resource):

    async def render_get(self, request):
        temperature = round(random.uniform(20, 35), 2)
        humidity = round(random.uniform(40, 80), 2)

        payload = f"Temperature={temperature}C, Humidity={humidity}%"
        print(f"[SERVER] GET → {payload}")

        return Message(payload=payload.encode())

    async def render_post(self, request):
        data = request.payload.decode()
        print(f"[SERVER] POST ← {data}")

        return Message(code=Code.CHANGED, payload=b"ACK: Secure Data Received")


async def main():
    root = resource.Site()
    root.add_resource(['sensor'], SensorResource())

    print("[SERVER] Running at coap://localhost:5683/sensor")

    await Context.create_server_context(root, bind=('localhost', 5683))
    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())