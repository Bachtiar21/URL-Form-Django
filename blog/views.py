from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

def index(request):
    db = Post.objects.all()
    context = {
        'Judul' : 'My Blog',
        'h1' : 'About me',
        'Nama' : 'Bachtiar Ramadhan',
        'NPM' : '1204077',
        'Asal' : 'Kuningan, Jawa Barat',
        'Email' : 'bachtiarramadhan26@gmail.com',
        'HP' : '085213921331',
        'Umur' : '22',
        'Desc' : 'Murid seumur hidup',
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
    }

    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse("RECENT BLOG")
    #context = {
    #    'Judul' : 'blog2',
    #    'h1' : 'Python'
    #}
    #return render(request, 'blog/index.html', context)
# Create your views here