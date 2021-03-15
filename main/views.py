from django.http import HttpResponse
from main import models
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import datetime

def home(request):
    return HttpResponse("Hello, Django!")

class Test_api(APIView):
    def post(self,request):
        print("request accepted")
        return Response({"data":"Ravi"})

class websocket(WebsocketConsumer):
    # def connect(self):
    #     self.accept()

    # def disconnect(self, close_code):
    #     pass

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     self.send(text_data=json.dumps({
    #         'message': message
    #     }))

    def connect(self):
        self.room_group_name = "ravi"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))