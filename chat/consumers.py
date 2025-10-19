from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
from .models import *
import json

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        # get the loggedin user
        self.user = self.scope['user']
        # get the chatroom name from the url route
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        self.chatroom=get_object_or_404(ChatGroup, group_name=self.chatroom_name)

        # after adding channels layers ion the settings.py file
        # we can use the channel layer in our consumer
        #making it async function
        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name,
            self.channel_name
        )
        self.accept()
        
        #add online users in the group
        #check if user is online or not
        
        if self.user not in self.chatroom.users_online.all():
           self.chatroom.users_online.add(self.user)
           self.update_online_count()
           
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name,
            self.channel_name
        )
        
        #remove user to online users in the group
        #check if user is online or not
        
        if self.user in self.chatroom.users_online.all():
           self.chatroom.users_online.remove(self.user)
           self.update_online_count()
        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json['body']
        
        message = GroupMessage.objects.create(
            body=body,
            author=self.user,
            group=self.chatroom
        )
        
        event = {
            "type":"message_handler",
            "message_id": message.id,
        }
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name,event
        )
        
    def message_handler(self, event):
        message_id = event['message_id']
        message=GroupMessage.objects.get(id=message_id)
        
        context={
           "message": message, 
           "user": self.user
        }
        
        html= render_to_string("chat/partials/chat_message_p.html", context=context)
        self.send(text_data=html)
        
    def update_online_count(self):
        online_count= self.chatroom.users_online.count()
        
        print ("Online count:", online_count)
        event={
            "type":"online_count_handler",
            "online_count": online_count,
        }
        
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name, event
        )
        
    def online_count_handler(self, event):
        online_count = event['online_count']
        html = render_to_string("chat/partials/online_count_p.html", context={'online_count': online_count})
        self.send(text_data=html)
            
            
            