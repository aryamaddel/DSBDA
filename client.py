# /// script
# dependencies = ["aiocoap"]
# ///

import asyncio
import random
from aiocoap import Context, Message
from aiocoap.numbers.codes import Code

def generate_data():
    temp = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2)
    return f"Temperature={temp},Humidity={humidity}"

async def main():
    context = await Context.create_client_context()

    while True:
        data = generate_data()

        print(f"[CLIENT] Sending POST: {data}")

        request = Message(
            code=Code.POST,
            uri="coap://localhost:5683/sensor",
            payload=data.encode()
        )

        try:
            response = await context.request(request).response
            print(f"[CLIENT] Response: {response.payload.decode()}")
        except Exception as e:
            print("[CLIENT] Error:", e)

        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())