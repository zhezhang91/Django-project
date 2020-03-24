from django.shortcuts import render
posts = [
    {
        'author': 'CoreMs',
        'title': 'Blog Post 1',
        'date_posted': 'Aug 29,2019'
    },
    {
        'author': 'Ma',
        'title': 'Blog Post 2',
        'date_posted': 'Aug 30,2019'
    }
]
# Create your views here.


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
