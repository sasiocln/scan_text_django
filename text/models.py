from django.db import models


class Photo(models.Model):
    lang = (
        ('rus', ('russian')),
        ('eng', ('english')),
    )
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    language = models.CharField(max_length=12, choices=lang, default='eng')
    text_of_image = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)
