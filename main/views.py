from django.http import HttpResponse
from main import models
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import datetime

def home(request):
    return HttpResponse("Hello, Django!")

class Test_api(APIView):
    def post(self,request):
        print("request accepted")
        return Response({"data":"Ravi"})