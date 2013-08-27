from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.tag_name)


class Blog(models.Model):
    """docstring for Blogs"""
    user = models.ForeignKey(User)
    caption = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    tag = models.ForeignKey(Tag)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    com_count = models.IntegerField(blank=True,null=True)
    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)
    class Meta:
        ordering = ['-publish_time']


class Comment(models.Model):
    """docstring for Comments"""
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    content = models.TextField(max_length=500)
    cmt_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.content)
    class Meta:
        ordering = ['-cmt_time']

