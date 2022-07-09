"""
Consumers config to handle events such as users connecting, disconnecting,
and sending messages.
Uses Websocket to detect inputs from users in the browser. Each user has
their own dedicated consumer
"""

import random
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        '''Code to run when a user connects to the room.
        Adds the user to the specified room and assigns a random username
        '''
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Give the user a random username
        self.username = "User" + str(random.randint(1, 50))
        await self.accept()

    async def disconnect(self, close_code):
        """Code to run when a user leaves the room"""
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """Receives and handles messages from WebSocket. 
        Sends a message to the group and echoes it locally to the user.
        Arguments:
          `text_data`: The message sent by the user
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message.startswith("/name"):
            self.username = message[5:].strip()
            await self.send(text_data=json.dumps({
                'message': "Changed username to " + self.username
        
            }))
        else:
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': self.username + ": " + message
                }
            )

    async def chat_message(self, event):
        """Receives and handles messages from the room group.
        This shows messages sent by other users.
        Arguments:
          `event`: The message sent by another user to display
        """
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))