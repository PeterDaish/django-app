from io import BytesIO
from faceApp.FastAgingGAN.infer import predict
from django.shortcuts import render
# Create your views here.
from django.http import FileResponse, response
from PIL import Image
from .FastAgingGAN.infer import predict
from django.http import HttpResponse
from .models import *
from .forms import *
import base64
import urllib.request
import pdb; 
def index(request):
    #webText = "Hello there! Thank you for finding this page." + " " + " Within this page, you will be able to try a DeepFake aging system first-hand, please proceed to the text below:"
    
    if request.method =='POST' and 'run_script_default_celebA' in request.POST:
        #import function to run
        print("Performing Inference")
        #get uploaded image and pass it into function.
        urllib.request.urlretrieve(
            'https://www.apzomedia.com/wp-content/uploads/2020/03/Tom-Cruise-Net-Worth-e1585322225367.jpg',
            "gfg.png")
  
        image = Image.open("gfg.png")
        #image = Image.open('/FastAgingGAN/images/TomCruise01.jpg')
        print("opened image")
        #call function to run.
        pdb.set_trace() 

        aged_image=predict(image)
        print("inferenced image")
        #return created image through HTTPResponse.
        
        #https://stackoverflow.com/questions/64203460/trying-to-display-image-in-web-page-generated-by-django-view
        
        buffered=BytesIO()
        print("saving locally as png")
        aged_image.save(buffered, format='png')
        print("first image save")
        im = Image.open(buffered)
        print("second image open")
        buffered2 = BytesIO()
        im.save(buffered2, format='png')
        print("second image save")
        im_str = base64.b64encode(buffered2.getvalue()).decode()
        data_uri = 'data:image/png;base64,'
        data_uri += im_str
        context = dict()
        context['data'] = data_uri
        print("base64 workded")

        return render(request, 'faceApp/result.html', context)


    if request.method =='POST' and 'run_script_default_celebB' in request.POST:
        #import function to run
        print("Performing Inference")
        #get uploaded image and pass it into function.
        urllib.request.urlretrieve(
            'https://th.bing.com/th/id/OIP.5sD893_i6DkMEJwBalTsZgHaHa?pid=ImgDet&rs=1',
            "gfg.png")
  
        image = Image.open("gfg.png")
        #image = Image.open('/FastAgingGAN/images/TomCruise01.jpg')
        print("opened image")
        #call function to run.
        pdb.set_trace() 

        aged_image=predict(image)
        print("inferenced image")
        #return created image through HTTPResponse.
        
        #https://stackoverflow.com/questions/64203460/trying-to-display-image-in-web-page-generated-by-django-view
        
        buffered=BytesIO()
        print("saving locally as png")
        aged_image.save(buffered, format='png')
        print("first image save")
        im = Image.open(buffered)
        print("second image open")
        buffered2 = BytesIO()
        im.save(buffered2, format='png')
        print("second image save")
        im_str = base64.b64encode(buffered2.getvalue()).decode()
        data_uri = 'data:image/png;base64,'
        data_uri += im_str
        context = dict()
        context['data'] = data_uri
        print("base64 workded")

        return render(request, 'faceApp/result.html', context)


    if request.method =='POST' and 'run_script_default_celebC' in request.POST:
        #import function to run
        print("Performing Inference")
        #get uploaded image and pass it into function.
        urllib.request.urlretrieve(
            'https://th.bing.com/th/id/OIP.Of6nTk2iTm5okVEWM5YR-gHaI5?pid=ImgDet&rs=1',
            "gfg.png")
  
        image = Image.open("gfg.png")
        #image = Image.open('/FastAgingGAN/images/TomCruise01.jpg')
        print("opened image")
        #call function to run.
        pdb.set_trace() 

        aged_image=predict(image)
        print("inferenced image")
        #return created image through HTTPResponse.
        
        #https://stackoverflow.com/questions/64203460/trying-to-display-image-in-web-page-generated-by-django-view
        
        buffered=BytesIO()
        print("saving locally as png")
        aged_image.save(buffered, format='png')
        print("first image save")
        im = Image.open(buffered)
        #get rid of image
        buffered = None
        print("second image open")
        buffered2 = BytesIO()
        im.save(buffered2, format='png')
        print("second image save")
        im_str = base64.b64encode(buffered2.getvalue()).decode()
        #get rid of image
        buffered2 = None
        data_uri = 'data:image/png;base64,'
        data_uri += im_str
        im_str = None
        context = dict()
        context['data'] = data_uri
        print("base64 workded")

        return render(request, 'faceApp/result.html', context)



    if request.method=='POST':
        pdb.set_trace()
        inImg = request.FILES["filename"]
        inImg = Image.open(inImg)
        
        aged_image=predict(inImg)
        print("inferenced image")
        buffered=BytesIO()
        print("saving locally as png")
        #encoded = base64.b64encode(inImg).decode('ascii')
        aged_image.save(buffered, format='png')
        print("first image save")
        im = Image.open(buffered)
        print("second image open")
        buffered2 = BytesIO()
        im.save(buffered2, format='png')
        print("second image save")
        im_str = base64.b64encode(buffered2.getvalue()).decode()
        data_uri = 'data:image/png;base64,'
        data_uri += im_str
        context = dict()
        context['data'] = data_uri
        print("base64 workded")

        return render(request, 'faceApp/result.html', context)

        
    #tasks = Task.objects.all()
    #form = TaskForm()

    #context = {'tasks': tasks, 'form': form}
    return render(request, 'faceApp/list.html')


