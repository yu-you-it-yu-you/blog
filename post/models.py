from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name=u'类别名称')

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 't_category'
        verbose_name_plural = u'类别'
    def __unicode__(self):
        return  self.cname

class Tag(models.Model):
    tname = models.CharField(max_length=30, unique=True, verbose_name=u'标签名称')

    def __str__(self):
        return self.tname

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'

    def __unicode__(self):
        return self.tname

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name=u'帖子名称')
    desc = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_post'
        verbose_name_plural = u'帖子'


