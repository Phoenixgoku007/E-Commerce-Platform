from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType #importing contenttype from django for making generic relation
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)# when the user gets deleted all his likes will also gets deleted
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # for identifying type of object user likes
    object_id = models.PositiveIntegerField() # for referencing particulat object
    content_object = GenericForeignKey() # for reading a particulat object