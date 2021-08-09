from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from .models import *
from .forms import *
def index(request):
    #webText = "Hello there! Thank you for finding this page." + " " + " Within this page, you will be able to try a DeepFake aging system first-hand, please proceed to the text below:"
    
    if request.method =='POST' and 'run_script' in request.POST:
        #import function to run

        #get uploaded image and pass it into function.

        #call function to run.

        #return created image.

        return render(request, 'faceApp/result.html', context)

    tasks = Task.objects.all()
    form = TaskForm()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'faceApp/list.html', context)


def result(request):
    user_input_age = int(request.GET["age"])
    prediction = fake_model.fake_predict