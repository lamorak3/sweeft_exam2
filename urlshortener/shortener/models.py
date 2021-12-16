from django.db import models

import datetime

from django.utils import timezone

from .generate import shorten
# Create your models here.
class Short_Data(models.Model):
    url = models.URLField(max_length=250)#sawyisi url max 250 simbolo
    short_url = models.CharField(max_length=9, unique=True)
    #shemoklebuli versia max 9 simbolo
    accessed_times = models.PositiveIntegerField(default=0)
    #daklikebis raodenoba
    creation_date = models.DateTimeField(auto_now_add=True)
    #sheqmnis dro auto_now_add miutitebs parametrs obieqtis sheqmnisas
    
    def was_created_recently(self):
        if self.creation_date < timezone.now() - datetime.timedelta(days=30):
            self.delete()
    
    def __str__(self):
        return "Short Url for: {} is {}".format(self.url,self.short_url)
        #print
    
    def save(self, *args, **kwargs):
        #tu short_url parametri sheyvanili ar aris sheqmnas random short_url
        if not self.short_url:
            self.short_url = shorten(self)

        super().save(*args, **kwargs)