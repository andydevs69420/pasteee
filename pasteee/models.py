from django.db import models
from .tools import uploadDate , expiryDate

# Create your models here.

class ImageLink(models.Model):

    # rely on autogen | auto_inc id

    # Non nullable
    img_link = models.FileField(
                upload_to = 'uploads/',
                blank = False,
                max_length = 1000,
              )

    # image uploaded field
    # uses date string instead
    img_upl  = models.CharField(
                blank   = False,
                default = uploadDate(),
                max_length = 10
             )
    # image expiration field
    # uses date string instead
    img_exp  = models.CharField(
                blank   = False,
                default = expiryDate(),
                max_length = 10
              )

