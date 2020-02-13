from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post,Comment,Profile,Like
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from .forms import PostForm

# Create your views here.
def home_page(request):
  title = 'Insta'
  return render(request, 'homepage.html',{"title":title})

@method_decorator(login_required, name='dispatch')
class SiteView(View):
  def get(self, request):
    posts = Post.objects.all()
    return render(request,'insta.html', {'posts':posts})

@login_required(login_url='login')
def new_post(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
        return redirect('insta')

    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form, "current_user":current_user})

def registration(request):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')

  context = {'form':form}
  return render(request, 'signup.html', context)