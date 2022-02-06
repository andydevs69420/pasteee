from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect

from .forms import ImageForm
from .models import ImageLink


from .tools import getFileName

# Create your views here.

def upload_file_view(request , *args , **kwargs):
    
    # backend heere!

    form = ImageForm()

    return render(request , 'pasteee/upload_file_view.html',{'form':form})

def on_upload(request):

    form = None
    ctx  = {}

    if  request.method == "POST":
        form = ImageForm(request.POST or None,request.FILES)

        if  not form.is_valid():
            # form has error
            return HttpResponseRedirect('/')

        form.save()

    else:
        form = ImageForm()
    
    latest_itm = ImageLink.objects.latest('id')

    link  = latest_itm.img_link
    name = getFileName(link)
    
    return HttpResponseRedirect(f"/viewer/?file={name}")


def viewer(request):

    ctx = {}

    if  request.method == "GET":

        if  request.GET['file'] != None:
            
            ctx['file'] = request.GET['file']

    return render(request,'pasteee/image_view.html',ctx)