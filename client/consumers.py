import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TickerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        stock_code = data.get('stockCode')
        # Example: Broadcast data back
        await self.send(text_data=json.dumps({
            'stockCode': stock_code,
            'price': 1234.56  # Dummy price; replace this with the actual stock price
        }))
