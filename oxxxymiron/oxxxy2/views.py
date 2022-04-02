from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout


def main(request):
	news = News.objects.all()[:3]
	traks = Trak.objects.all()[:3]
	albums = Album.objects.all()[:3]

	return render(
		request, 'oxxxy2/index.html', {'news': news, 'traks': traks, 'albums': albums}
	)


class NewsList(ListView):
	model = News
	template_name = 'oxxxy2/news.html'
	context_object_name = 'news'


def traks(request):
	traks = Trak.objects.all()
	return render(request, 'oxxxy2/traks.html', {'traks': traks, 'title': 'треки'})


class Albums(ListView):
	model = Album
	template_name = 'oxxxy2/albumlist.html'
	context_object_name = 'albums'


class DetailTrak(DetailView):
	model = Trak
	template_name = 'oxxxy2/trakdetail.html'
	context_object_name = 'trak'


class DetailNews(DetailView):
	model = News
	template_name = 'oxxxy2/newsdetail.html'
	context_object_name = 'news'


class DetailAlbum(DetailView):
	model = Album
	template_name = 'oxxxy2/albumdetail.html'
	context_object_name = 'album'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['album_traks'] = self.object.trak_set.all()

		return context


class NewsForm(CreateView):
	form_class = CreateNewsForm
	template_name = 'oxxxy2/newsform.html'


class Register(CreateView):
	form_class = UserRegister
	template_name = 'oxxxy2/register.html'
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('main')


class Login(LoginView):
	form_class = UserAuthentication
	template_name = 'oxxxy2/login.html'


def logout_user(request):
	logout(request)
	return redirect('main')

