#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from sblog.models import Blog, Tag ,Comment


class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'id', 'user', 'publish_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)

class CommentAdmin(admin.ModelAdmin):
    """docstring for CommentAdmin"""
    list_display = ('user','blog','content','cmt_time')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
