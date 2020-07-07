from django.test import TestCase
from django.urls import reverse,resolve
from ..views import home,blog_topics,new_topic
from ..models import Blog

#主页测试
class HomeTests(TestCase):

    def setUp(self):
        self.blog = Blog.objects.create(name='Django', description='Django Blog.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        blog_topics_url = reverse('blog_topics', kwargs={'pk': self.blog.pk})
        self.assertContains(self.response, 'href="{0}"'.format(blog_topics_url))

#Test 2
class BlogTopicsTests(TestCase):
    def setUp(self):
        Blog.objects.create(name='Django', description='Django blog.')

    def test_Blog_topics_view_success_status_code(self):
        url = reverse('blog_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_Blog_topics_view_not_found_status_code(self):
        url = reverse('blog_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_Blog_topics_url_resolves_Blog_topics_view(self):
        view = resolve('/blogs/1/')
        self.assertEquals(view.func, blog_topics)



class NewTopicTests(TestCase):
    def setUp(self):
        Blog.objects.create(name='Django', description='Django Blog.')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/blogs/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_Blog_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        blog_topics_url = reverse('blog_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(blog_topics_url))
