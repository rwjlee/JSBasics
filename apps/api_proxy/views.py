import json, requests

from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'api_proxy/index.html')

def data(request):
    if request.method == 'POST':
        try:
            return JsonResponse(requests.get(request.POST['url']).text, safe=False)
        except:
            return JsonResponse({'error': 'Request failed'})

    return JsonResponse({'error': 'GET request not allowed'})

def demo(request):

    return render(request, 'api_proxy/demo.html')