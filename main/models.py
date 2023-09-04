import random
from multiupload.fields import MultiFileField, MultiImageField
from django.db import models

# Create your models here.
class cloud(models.Model):
    title = models.CharField('Title', max_length=50)
    ident = models.IntegerField('Code')
    text = models.TextField('Text')
    file = models.FileField('File', upload_to='Files')
    #file = MultiFileField()
   # file = models.MultiFileField('File', upload_to='Files', max_file_size=1024 * 1024 * 15, max_upload_count=5)
    image = models.ImageField('Image', upload_to='Files')
    date = models.DateTimeField('Time', auto_now_add=True)

    def file_upload_to(instance, filename):
        return f'Files/{filename}'

    file.upload_to = file_upload_to

    def save(self, *args, **kwargs):
        all_clouds = cloud.objects.all()
        if not self.pk:  # Если объект только что создан
            self.ident = random.randint(100000, 1000000)
            while(not self.checkId(all_clouds)):
                self.ident = random.randint(100000, 1000000)

        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    def checkId(self, all_clouds):
        for el in all_clouds:
            if (el.ident == self.ident):
                return False
        return True