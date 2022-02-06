
from django.urls import path
from .views import upload_file_view , on_upload,viewer


urlpatterns = [
    path('' , upload_file_view    , name = 'upload_file_view' ),
    path('on_upload/' , on_upload , name = 'on_upload'),
    path('viewer/'    , viewer    , name = 'viewer'),
]


