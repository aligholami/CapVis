from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import os

# principal data paths
data_dir = 'C:/Users/hexph/Desktop/CapVis/data'

cap_dir = os.path.join(data_dir, 'captioning_experiments/{}')
match_dir = os.path.join(data_dir, 'matching_experiments/{}')

cap_exp_list = os.listdir(os.path.join(data_dir, 'captioning_experiments'))
match_exp_list = os.listdir(os.path.join(data_dir, 'matching_experiments'))

def index(request):
    return HttpResponse("Hell and welc.")

def captions(request):
    return JsonResponse(cap_exp_list, safe=False)

def matches(request):
    return JsonResponse(match_exp_list, safe=False)

def get_cap(request):
    exp_info = ['pred_train.json', 'pred_val.json', 'log.txt', 'best.txt']
    requested_experiment_name = request.GET.get('exp_name') # image_stacked_attention for example
    
    experiment_directory = cap_dir.format(requested_experiment_name)

    response_dict = {}
    for ei in exp_info:
        ei_path = os.path.normpath(os.path.join(experiment_directory, ei))
        if '.json' in ei:
            ef = json.load(open(ei_path))
        elif '.txt' in ei:
            ef = open(ei_path).readlines()
        else:
            ef = None

        response_dict[ei] = ef
        
    return JsonResponse(response_dict, safe=False)

def get_match(request):
    exp_info = ['matches_train.json', 'matches_val.json']
    requested_experiment_name = request.GET.get('exp_name') # v1.0 for example
    
    experiment_directory = os.path.normpath(match_dir.format(requested_experiment_name))

    response_dict = {}
    for ei in exp_info:
        ei_path = os.path.join(experiment_directory, ei)
        if '.json' in ei:
            ef = json.load(open(ei_path))
        elif '.txt' in ei:
            ef = open(ei).readlines()
        else:
            ef = None

        response_dict[ei] = ef
        
    return JsonResponse(response_dict, safe=False)
