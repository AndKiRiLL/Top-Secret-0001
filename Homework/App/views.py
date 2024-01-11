from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Category, Post
from .forms import FormCreate, FormEdit
from django.views.generic import ListView, CreateView, FormView, DeleteView, UpdateView
from django.urls import reverse_lazy

class AddPage(CreateView):
    form_class = FormCreate
    template_name = 'app/Form_create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def post(self, request):
        if request.method == "POST":
            post = Post()
            post.name = request.POST.get("name")
            post.caption = "---"
            post.img = request.POST.get("img")
            post.category_id = request.POST.get("category")
            post.author_id = request.POST.get("author")
            post.date = request.POST.get("date")
            post.save()
            return HttpResponseRedirect("/")

class DeletePage(DeleteView):
    model = Post
    template_name = 'app/delete.html'
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class EditPage(UpdateView):
    model = Post
    form_class = FormEdit
    template_name = 'app/edit.html'
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            if request.method == "POST":
                post.name = request.POST.get("name")
                post.caption = "---"
                post.img = request.POST.get("img")
                post.category_id = request.POST.get("category")
                post.author_id = request.POST.get("author")
                post.date = request.POST.get("date")
                post.save()
                return HttpResponseRedirect("/")

        except Post.DoesNotExist:
            return HttpResponseNotFound("<h2>Post not found</h2>")


def initialize():
    if Category.objects.all().count() == 0:
        Category.objects.create(name="Политика")
        Category.objects.create(name="Экономика")
        Category.objects.create(name="Спорт")
        Category.objects.create(name="Кулинария")
        Category.objects.create(name="Природа")
        Category.objects.create(name="Строительство")

####################### Page Home #######################

class PageHome(ListView):
    model = Category
    template_name = 'app/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

####################### Page Political #######################
class PagePolitical(ListView):
    model = Category
    template_name = 'app/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=2)
        return context

####################### Page Economic #######################
class PageEconomic(ListView):
    model = Category
    template_name = 'app/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=3)
        return context

####################### Page Sport #######################
class PageSport(ListView):
    model = Category
    template_name = 'app/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=4)
        return context

####################### Page Cooking #######################
class PageCooking(ListView):
    model = Category
    template_name = 'app/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=5)
        return context

####################### Page Nature #######################
class PageNature(ListView):
    model = Category
    template_name = 'app/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=6)
        return context

####################### Page Construction #######################
class PageConstruction(ListView):
    model = Category
    template_name = 'app/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=7)
        return context
