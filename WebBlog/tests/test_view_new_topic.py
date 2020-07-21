#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 22:35
# @Author : ZhangYongjie

from django.test import TestCase
from django.urls import reverse
from ..models import Blog

class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        Blog.objects.create(name='Django', description='Django blogs.')
        self.url = reverse('new_topic', kwargs={'pk': 1})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))