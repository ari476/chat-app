from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def a(request):
    return JsonResponse(3, safe=False)