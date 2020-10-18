from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import os

# principal data paths
data_dir = 'C:/Users/hexph/Desktop/CapVis/data'
cap_exp_list = os.listdir(os.path.join(data_dir, 'captioning_experiments'))
match_exp_list = os.listdir(os.path.join(data_dir, 'matching_experiments'))

def index(request):
    return HttpResponse("Hell and welc.")

def captions(request):
    return JsonResponse(cap_exp_list, safe=False)

def matches(request):
    return JsonResponse(match_exp_list, safe=False)