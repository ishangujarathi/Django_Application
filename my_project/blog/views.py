from django.shortcuts import render

posts = [
    {
        'author' : 'Ishan Gujarathi',
        'title' : 'Blog Post 1',
        'content' : 'First_Post_Content',
        'date_posted' : 'January 30, 2024',
    },

    {
        'author' : 'Akshat Gujarathi',
        'title' : 'Blog Post 2',
        'content' : 'Second_Post_Content',
        'date_posted' : 'January 30, 2024',
    },

]

def home(request):

    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html', {'title':'about'})


