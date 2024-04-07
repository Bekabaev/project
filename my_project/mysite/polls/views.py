from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    post_data = Post.objects.all()
    context = {
        "post_data" : post_data
    }
    return render(request,"polls/index.html", context)