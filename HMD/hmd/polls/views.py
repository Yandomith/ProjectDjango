from django.http import HttpResponse
from django.shortcuts import render 
from .models import Post


def index(request):
    postList= Post.objects.order_by("postDate")
    context = {"postList":postList}
    return render(request,"index.html", context)
    
# def index(request):
#     return render(request, "index.html")