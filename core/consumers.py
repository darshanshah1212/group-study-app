import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from .models import ChatMessage
from asgiref.sync import sync_to_async

class MyStudyGrp(AsyncWebsocketConsumer):
    async def connect(self):
        print("Client Connected...")

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
        
        print(f"Connected to the room {self.room_group_name}")
        
    async def disconnect(self):
        print("Client disconnected ...")
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
        StopConsumer()
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message","")

        await self.save_message(self.room_name,'Annonymous',message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chat_send",
                "message" : message,
                "user":"Annonymous"
            }
        )
        
        print("Data recived from the client ",data) 
        
    async def chat_send(self,event):
        await self.send(text_data=json.dumps({
            "user":event["user"],
            "message":event["message"]
        }))
        
    @sync_to_async
    def save_message(self,room,user,content):
        return ChatMessage.objects.create(room=room,user=user,content=content)
    