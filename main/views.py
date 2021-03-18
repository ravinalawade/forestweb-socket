from django.http import HttpResponse
from main import models
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import datetime
# import routing
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def home(request):
    return HttpResponse("Hello, Django!")

class Test_api(APIView):
    def post(self,request):
        print("request accepted")
        async_to_sync(get_channel_layer().group_send)(
            "pratik",
            {
                'type': 'send_message',
                'message': "I am Ravi"
            }
        )
        return Response({"data":"Ravi"})