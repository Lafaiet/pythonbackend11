import random
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from viewer.models import Movie, Actor
from viewer.forms import ContactForm, SignUpForm


def hello(request):
    content = '<b>Hello world! I am learning Django!</b>'

    return HttpResponse(content)


def luck_number(request):
    number = random.randint(1, 10)
    content = f'Your lucky number is {number}'

    return HttpResponse(content)


def favorite_pet(request):
    pet = request.GET.get('mypet')

    if pet is None:
        content = 'You do not like any pets :('
    else:
        content = f'Your favorite pet is {pet} :)'

    return HttpResponse(content)


def pet_names(request, pet_type):
    if pet_type == 'dog':
        names = ['Lulu', 'Muki', 'Zeus', 'Thor', 'Odin']

    elif pet_type == 'cat':
        names = ['Mimi', 'Garfield', 'Felix', 'Miisu', 'Meow']

    else:
        content = f'Sorry. We do not have any suggestion for {pet_type} at the moment'
        return HttpResponse(content)

    content = 'Here are some suggestions for you: ' + ', '.join(names)

    return HttpResponse(content)


def home_page(request):

    context = {
        'page_name': 'Home Page'
    }
    return render(request, template_name='home.html', context=context)


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_name'] = 'Home Page'

        return context


class MoviesList(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_name'] = 'Movies List'

        return context


class MovieDetail(DetailView):
    template_name = 'detail_movie.html'
    model = Movie
    context_object_name = 'movie'


class MovieCreate(PermissionRequiredMixin, CreateView):
    template_name = 'create_movie.html'
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies_list')
    permission_required = 'viewer.add_movie'


class MovieUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'update_movie.html'
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies_list')
    permission_required = 'viewer.change_movie'


class MovieDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_movie.html'
    model = Movie
    success_url = reverse_lazy('movies_list')
    context_object_name = 'movie'
    permission_required = 'viewer.delete_movie'


class Contact(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_data = form.cleaned_data
        print(form_data)

        return super().form_valid(form)


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    form_class = SignUpForm


