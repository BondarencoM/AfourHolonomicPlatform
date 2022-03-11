import json
from arfourWeb.machineControl.MachineController import MachineControl
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import csrf_exempt

machine = MachineControl()


def index(request):
    return render(request, 'holonomic/index.html')


@csrf_exempt
def arbitraryMove(request: WSGIRequest):
    data = json.loads(request.body)
    machine.arbitraryMove(data['angle'], data['speed'])
    return JsonResponse({
        'status': 'OK'
    })

@csrf_exempt
def presetMove(request: WSGIRequest):
    data = json.loads(request.body)
    machine.presetMove(data['moveId'])
    return JsonResponse({
        'status': 'OK'
    })
