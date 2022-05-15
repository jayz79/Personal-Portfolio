from django.shortcuts import render, get_object_or_404
from .models import Blog, Video
from .forms import VideoForm


# Returns all blogs from db
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

# Returns info of desired blog with its blog_id
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})

# Returns most recently uploaded video 
def show_video(request):
    latest_video = Video.objects.last()
    video_file = latest_video.video_file