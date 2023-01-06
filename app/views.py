from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def create(request):
    context = {}
    return render(request, 'app/create.html', context)

def vote(request, poll_id):
    context = {}
    return render(request, 'app/vote.html', context)

def results(request, poll_id):
    context = {}
    return render(request, 'app/results.html', context)