from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    if request.method == 'GET':
        if 'gold' not in request.session:
            request.session['gold'] = 0
        if 'text' not in request.session:
            request.session['text'] = []
        content = {
            'gold': request.session['gold'],
            'text': request.session['text'],
        }
    return render(request, "ninja_app/index.html", content)

        
def process_money(request):
    if request.method == 'POST':
        locations = {
            'farm': [10, 20],
            'cave': [5, 10],
            'house': [2, 5],
            'casino': [-50, 50]
        }
        for key in locations:
            if key == request.POST['candy']:
                temp_dict = random.randint(locations[key][0], locations[key][1])
                request.session['gold'] += temp_dict
                if temp_dict >= 0:
                    request.session['text'].append("<p class='positive'>You earned " + str(temp_dict) + " gold coins from the " + key + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                else:
                    request.session['text'].append("<p class='negative'>You lost " + str(temp_dict) + " gold coins from the " + key + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
