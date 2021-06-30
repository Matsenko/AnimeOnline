# from django.urls import path
from django.urls.conf import include
from . import views

# urlpatterns = [
#     path('',views.index,name='index'),
#     # path('<int:anime_id>/',views.detail,name='detail')
# ]
from django.urls import path,include

from .views import AnimeView, Profile,RegisterView,ProfileEditingView
app_name = "anime_list"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    # path('anime_list/', AnimeView.as_view()),
    path('', views.home, name='home'),
    path('accounts/profile/',views.Profile,name='profile'),
    path('accounts/profile/editing',views.ProfileEditingView,name='profile_editing'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('api/',AnimeView.as_view()),
    path('anime_list/',views.AnimeList,name='AnimeList'),
    path('',include('social_django.urls')),
  
    # path('anime_list/<int:pk>', AnimeView.as_view()),

]
