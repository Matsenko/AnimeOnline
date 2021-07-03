import re
from django.shortcuts import render
# from .models import Anime_list,Anime_comment

# # def detail(request,anime_id):
# #     try:
# #         a=Anime_list.objects.get(id=anime_id)
# #     except:
# #         raise Http404("Статья не найдена!")
# #     return render(request,'anime_list/detail.html',{'anime':a})         
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Anime_list
from django.core import serializers
from .serializers import AnimeSerializer
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.conf import settings
def AnimeList(request):
    latest_anime_list=Anime_list.objects.order_by('-pub_date')[:10]
    return render(request,'anime_list/anime_list.html',{'latest_anime_list':latest_anime_list})
def home(request):
    latest_anime_list=Anime_list.objects.order_by('-pub_date')[:3]
    return render(request,'base.html',{'latest_anime_list':latest_anime_list})
def Profile(request):
    if request.user.is_authenticated:
        user_data=User.objects.all()
        return render(request,'profile/profile.html',{'user_data':user_data})
    else:
        return redirect('/')    

class AnimeView(APIView):
        def get(self, request):
            if (request.user.is_authenticated and request.user.is_superuser):
                anime_list = Anime_list.objects.all()
                serializer = AnimeSerializer(anime_list, many=True)
                return Response({"anime_list": serializer.data})
            else:
                return redirect('/')
        def post(self, request):
            if (request.user.is_authenticated and request.user.is_superuser):
                anime_list = request.data.get('anime_list')
        
                serializer = AnimeSerializer(data=anime_list)
                if serializer.is_valid(raise_exception=True):
                    anime_saved = serializer.save()
                return Response({"success": "Anime '{}' created successfully".format(anime_saved.title)})
            else:
                return redirect('/')   
     
class RegisterView(TemplateView):
    template_name = "registration/register.html"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            if request.method == 'POST':
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                password2 = request.POST.get('password2')

                if password == password2:
                    User.objects.create_user(username, email, password)
                    return redirect(reverse("login"))

            return render(request, self.template_name)   
        else:
            return redirect('/')

@login_required
def ProfileEditingView(request):
    try:
        if request.method == "POST":
            
            User.objects.filter(username=request.user.username).update(username=request.POST.get("username"))
            User.objects.filter(username=request.user.username).update(email=request.POST.get("email"))
            return redirect("/")
        else:
            return render(request, "profile/profile_editing.html")
    except User.DoesNotExist:
        return"<h2>User not found</h2>"      

def logout(request):
    django_logout(request)
    domain=settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id=settings.SOCIAL_AUTH_AUTH0_KEY
    return_to='http://127.0.0.1:8000'
    return redirect(f'https://{domain}/v2/logout?returnTo={return_to}&client_id={client_id}')