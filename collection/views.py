from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    # this is your new view
    return render_to_response('index.html')