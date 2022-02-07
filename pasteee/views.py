from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ImageForm
from .models import ImageLink


from .tools import hash, getFileName 

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
    id = hash(str(latest_itm.id))
    
    return HttpResponseRedirect(f"/viewer/?id={id}")


def viewer(request):

    ctx = {}

    if  request.method == "POST":
        return HttpResponseRedirect('/')

    else:
        
        if  'id' not in request.GET:
            pass

        try:
            gID  = hash(str(request.GET['id']),ishash = False)
            file = ImageLink.objects.get(id=gID)

            if  file:
                link = file.img_link
                name = getFileName(link.url)
                ctx['file'] = name

        except Exception as err:
            # consider error if the id is not 
            # base66 while convertion
            pass

    return render(request,'pasteee/image_view.html',ctx)