from django.db import models

class  Post(models.Model):
    write_dttm = models.DateTimeField(auto_now_add = True, verbose_name = '글 작성일')