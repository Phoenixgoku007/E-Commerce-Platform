from django.db import models
from django.contrib.contenttypes.models import ContentType #importing contenttype from django for making generic relation
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=255)



class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

# For implementing generic relationship these three fields are required

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()