from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Admin


def hello(req):
    return JsonResponse(
        {
            "data": [
                {
                    "id": i.id,
                    "username": i.username
                }
                for i in Admin.objects.all()
            ]
        }
    )
