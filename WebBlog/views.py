from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog,Topic,Post
from django.contrib.auth.models import User
from .forms import NewTopicForm,PostForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count


#主页


def home(request):
    # return HttpResponse('Hello, World!')
    blogs = Blog.objects.all()

    return render(request, 'Home.html', {'blogs': blogs})


 #127.0.01.8000/blogs 函数编写 在 urls.py中加入/blog 以便查询 相当于多级文件


def blog_topics(request,pk):
    blog = get_object_or_404(Blog,pk = pk)
    topics = blog.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    return render(request, 'topics.html',{'blog': blog,'topics':topics})




#127.0.0.0:8000/.../new   TODO：创建新博客，并提交上去
#调用 new_topic.html文件和forms.py form.html 文件  form.html文件为new_topics.html文件的错误提示与样式

@login_required
def new_topic(request,pk):
    blog = get_object_or_404(Blog, pk = pk)

    # user = User.objects.first()  # TODO: get the currently logged in user

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.blog = blog
            topic.starter = request.user
            topic.save()


            Post.objects.create(
                message=form.cleaned_data.get("message"),
                topic=topic,
                created_by = request.user
            )

            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)  # TODO: redirect to the created topic page

    else:
        form = NewTopicForm()

    return render(request,'new_topic.html',{'blog':blog,'form':form})



def topic_posts(request,pk, topic_pk):
    topic = get_object_or_404(Topic,blog__pk=pk, pk = topic_pk)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic':topic})

# 回复
@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic,blog__pk=pk,pk = topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk= pk, topic_pk= topic_pk)

    else:
        form = PostForm()

    return render(request,'reply_topic.html',{'topic':topic,'form':form})



