from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ModelPost, ModelProduct
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django")

class ViewModelProduct(ListView):
    queryset = ModelProduct.objects.all()
    template_name = 'products.html'

class ViewModelPost(ListView):
    queryset = ModelPost.objects.all()
    template_name = 'list.html'

class CreateModelPost(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = ModelPost
    fields = '__all__'
    template_name = 'create_comment.html'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect(reverse('list'))

class UpdateModelPost(UpdateView):
        model = ModelPost
        fields = ['content']
        template_name = 'update_ModelPost_form.html'

        def get_object(self, queryset=None):
                id = self.kwargs['id']
                return self.model.objects.get(id=id)

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('list'))

class DeleteModelPost(DeleteView):
        model = ModelPost
        template_name = 'delete_ModelPost_form.html'

        def get_success_url(self):
            return reverse('list')
