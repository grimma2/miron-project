from django.urls import path
from .views import *
from .models import *


urlpatterns = [
	path('news/', Newsd.as_view(), name = 'news'),
	path('traks/', trak, name = 'traks'),
	path('news/<str:slug>/', DetailNews.as_view(), name = 'detail_news'),
	#path('<slug:alubum_slug>', DetailA.as_view(), name = 'detail_albums'),
	path('newsform/createnews/sjehrlkrhtlj43uhtiu53yhi5yh4u', NewsForm.as_view(), name = 'formnews1'),
	path('user/register/', Register.as_view(), name = 'register'),
	path('user/login/', Login.as_view(), name = 'login'),
	path('user/logout/', logout_user, name = 'logout'),
]