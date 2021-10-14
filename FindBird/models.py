from django.db import models

# Create your models here.
class Bird(models.Model):
    bird_id = models.IntegerField(primary_key= True)
    slug = models.CharField(max_length=50)
    search_name = models.CharField(max_length=50, default="")
    Original_Name = models.CharField(max_length=50)
    Biological_Name = models.CharField(max_length=50)
    paragraph = models.TextField(default=None)
    paragraph2 = models.TextField(default=None)    
    paragraph3 = models.TextField(default=None)    
    image1 = models.ImageField(upload_to="FindBird/image1", default="")
    image2 = models.ImageField(upload_to="FindBird/image2", default="")
    map1 = models.ImageField(upload_to="FindBird/map", default="")
    record = models.FileField(upload_to="FindBird/audio", default="")

    def __str__(self):
        return self.Original_Name