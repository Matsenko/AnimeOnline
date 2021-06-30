from django.db import models
import datetime
from django.utils import timezone
class Anime_list(models.Model):
    anime_name=models.CharField('Anime name',max_length=200)
    anime_text=models.TextField('Anime description')
    pub_date=models.DateTimeField('Publication date')
    def __str__(self):
        return self.anime_name
    def  was_published_recently(self):
        return self.pub_date >= (timezone.now()-datetime.timedelta(days=7))     


class Anime_comment(models.Model):
    anime=models.ForeignKey(Anime_list,on_delete=models.CASCADE)
    author_name=models.CharField('Author name',max_length=50)
    comment_text=models.TextField('Comment') 
    pub_date=models.DateTimeField('Publication date')   
    def __str__(self):
        return self.author_name
