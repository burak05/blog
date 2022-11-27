from django.shortcuts import render,HttpResponse,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request=request,template_name="index.html")

def about(request):
    return render(request=request,template_name="about.html")

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request=request,template_name="dashboard.html",context=context)

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article Added")
        return redirect("index")
    return render(request=request,template_name="addarticle.html",context={"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    return render(request=request,template_name="detail.html",context={"article" : article})