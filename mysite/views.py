from django.shortcuts import render

# Create your views here.
def home_page(request):
  title = 'Insta'
  return render(request, 'homepage.html',{"title":title})