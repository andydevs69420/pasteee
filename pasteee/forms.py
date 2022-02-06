
from django import forms

from .models import ImageLink

class ImageForm(forms.ModelForm):

    class Meta:

        model  = ImageLink
        fields = ('img_link',)

        widgets = {
            'img_link' : forms.FileInput(
                # setup attributes for DOM
                attrs = { 
                    'type'   : 'file'        ,
                    'accept' : 'image/*'     ,
                    'id'     : 'file-pick'   ,
                    'class'  : 'file-picker' ,
                }
            )
        }
        labels = {
            'img_link' : ''
        }

