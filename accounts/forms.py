#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/13 19:24
# @Author : ZhangYongjie
"""
扩展  UserCreationForm  （该函数不提供 email 字段）
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')