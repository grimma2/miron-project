from django.urls import path
from .views import *


urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('traks/', traks, name='traks'),
    path('albums/', Albums.as_view(), name='albums'),
    path('trak/<str:slug>/', DetailTrak.as_view(), name='detail_trak'),
    path('news/<str:slug>/', DetailNews.as_view(), name='detail_news'),
    path('albums/<str:slug>/', DetailAlbum.as_view(), name='detail_album'),
    path('newsform/createnews/', NewsForm.as_view(), name='formnews'),
    path('user/register/', Register.as_view(), name='register'),
    path('user/login/', Login.as_view(), name='login'),
    path('user/logout/', logout_user, name='logout'),
]
