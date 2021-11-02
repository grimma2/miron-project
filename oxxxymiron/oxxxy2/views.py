from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.utils import timezone
from .forms import *
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout


def main(request):
	print(request)
	news = News.objects.all()[:3]
	trak = Trak.objects.all()[:3]
	albums = Album.objects.all()
	return render(request, 'oxxxy2/main.html', {'news': news, 'trak': trak, 'albums': albums, 'title': 'Главная страница'})

class Newsd(ListView):
	paginate_by = 4
	model = News
	template_name = 'oxxxy2/news.html'
	context_object_name = 'news1'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Новости'
		return context
	

def trak(request):
	print(request.user.first_name)
	trak1 = Trak.objects.all()
	return render(request, 'oxxxy2/traks.html', {'trak1': trak1, 'title': 'треки'})

class DetailNews(DetailView):
	model = News
	template_name = 'oxxxy2/newsdetail.html'
	context_object_name = 'detail_news1'

	def get_context_data(self, **kwargs):
		slug = self.object.get_absolute_url(self.object.slug)
		context = super().get_context_data(**kwargs)

		return context





class NewsForm(CreateView):
	form_class = CreateNewsForm
	template_name = 'oxxxy2/newsform.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Добавление Новости'
		return context

class Register(CreateView):
	form_class = UserRegister
	template_name = 'oxxxy2/register.html'
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		print(**form.cleaned_data)
		return redirect('main')


class Login(LoginView):
	form_class = UserAuthentication
	template_name = 'oxxxy2/login.html'


def logout_user(request):
	logout(request)
	return redirect('main')

