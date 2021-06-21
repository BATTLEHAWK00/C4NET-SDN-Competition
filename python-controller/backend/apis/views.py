from django.shortcuts import render

# Create your views here.
from utils.JsonResponse import get_response
from sdn_controller_api.apis import controller


def hello(req):
    return get_response({"msg": "测试"})


def get_topology(req):
    return get_response(controller.get_topology())
