from django.shortcuts import render
from .models import Post

def home(request):

    context = {
        'posts': Post.objects.all()  #directly fetching the data from the Post Database that was created in the models.py file
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html', {'title':'about'})


