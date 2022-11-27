from django.shortcuts import render,HttpResponse
from .forms import ArticleForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request=request,template_name="index.html")

def about(request):
    return render(request=request,template_name="about.html")

def dashboard(request):
    return render(request=request,template_name="dashboard.html")

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article Added")
        return redirect("index")
    return render(request=request,template_name="addarticle.html",context={"form":form})