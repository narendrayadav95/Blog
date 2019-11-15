from django.shortcuts import render
from coreyschafer.models import Post

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post1',
#         'content': 'First Post Content',
#         'date_posted': 'Aug 27, 2018',
#     },
# {
#         'author': 'Narendra',
#         'title': 'Blog Post2',
#         'content': 'Second Post Content',
#         'date_posted': 'Aug 27, 2018',
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})