import asyncio
import array
from bleak import BleakClient

address = "E43D4199-EB93-DBE8-4565-0E8F0C3202A1"
UUID_NORDIC_TX = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
UUID_NORDIC_RX = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
command = b"\x03\x10 var result = E.getTemperature();\n\x10print(result)\n" ## Get temperature level of the Watch.

def uart_data_received(sender, data):
  print("RX> {0}".format(data))
 
print("Connecting...")

async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        print("Connected")
        
        await client.start_notify(UUID_NORDIC_RX, uart_data_received)
        
        
        print("Writing command")
        c = command
        while len(c) > 0:
            await client.write_gatt_char(UUID_NORDIC_TX, bytearray(c[0:10]), True)
            c = c[10:]
        print("Waiting for data")
        
        await asyncio.sleep(1.0)  # wait for a response
       
        print("Done!")

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))
