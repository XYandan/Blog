#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/5 21:09
# @Author : ZhangYongjie
"""
定义输入文本的样式之类的 并在views.py文件中import

同时使用了Django.forms API   ->  https://docs.djangoproject.com/en/3.0/topics/forms/

构建表单以接受来自站点访问者的输入，然后处理并响应输入
"""

from django import forms
from .models import Topic,Post

class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
            attrs={'rows': 5, 'placeholder': 'Input your article title'}
        ),
    max_length=30)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the message is 4000.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]