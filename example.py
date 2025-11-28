from deltaton_py.index import DeltatonFeedClient
import asyncio
import math
import random
import json

async def handle_response(data):
  print('Response received:')
  print(json.dumps(data, indent=2))

async def main():
  token = 'YOUR_DELTATON_FEED_TOKEN'
  user_id = 'YOUR_DELTATON_USER_ID'
  farm_id = 'YOUR_FARM_ID'
  deltaton_feed = DeltatonFeedClient(token, user_id)
  await deltaton_feed.connect()

  while True:
    data = {
      'temperature': math.floor(random.random() * 100),
      'temperatureUnit': 'celsius',
      'humidity': math.floor(random.random() * 100),
    }
    await deltaton_feed.emit_myfarm(data, farm_id, handle_response)
    await asyncio.sleep(60)

if __name__ == '__main__':
  asyncio.run(main())

