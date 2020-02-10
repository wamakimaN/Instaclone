from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post,Comment,Profile,Like
from django.views import View
from django.views.generic.list import ListView

# Create your views here.
def home_page(request):
  title = 'Insta'
  return render(request, 'homepage.html',{"title":title})

@method_decorator(login_required, name='dispatch')
class SiteView(View):
  model = Post
  template_name = 'insta.html'