import asyncio
import array
from bleak import discover
from bleak import BleakClient
from bleak import BleakScanner


# ### Get the device name/Discover the avaliable devices
# async def scanBangle():
#     devices = await BleakScanner.discover()
#     for device in devices:
#         print(device)
# asyncio.run(scanBangle())


# address = "d6:04:c8:27:c9:10" ### MacBook doesnot give Mac Address, instead it gives UUID
address = "E43D4199-EB93-DBE8-4565-0E8F0C3202A1"



print("Connecting...")

async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        
        print(client.is_connected) ## this gives true or false
        print("Connected")
        await asyncio.sleep(1.0) # wait for a response
        print("Done!")
        print()
        print(f"Name: {client.services}")
        print(f"Address: {client.address}")
        print(f"Details: {client.services}")
        print(f"Metadata: {client.address}")
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))