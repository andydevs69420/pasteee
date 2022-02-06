from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def upload_file_view(request , *args , **kwargs):
    
    # backend heere!

    return render(request , 'pasteee/upload_file_view.html')

def on_upload(request):

    if  request.method == "POST":
        print(request.method)

    return HttpResponse("FOOCC!!")