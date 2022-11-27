from django.shortcuts import render,HttpResponse,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains =keyword)
        return render(request=request,template_name="articles.html",context={"articles":articles})
    articles = Article.objects.all()
    
    return render(request=request,template_name="articles.html",context={"articles":articles})

def index(request):
    return render(request=request,template_name="index.html")

def about(request):
    return render(request=request,template_name="about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request=request,template_name="dashboard.html",context=context)
@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article Added")
        return redirect("article:dashboard")
    return render(request=request,template_name="addarticle.html",context={"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    return render(request=request,template_name="detail.html",context={"article" : article,"comments":comments})
@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article Updated")
        return redirect("article:dashboard")
    return render(request=request,template_name="update.html",context={"form":form})
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Article Deleted")
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author") 
        comment_content = request.POST.get("comment_content") 
        newComment = Comment(comment_author = comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))