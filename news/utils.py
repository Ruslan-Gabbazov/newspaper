from django.db import models
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from django import forms
from django.urls import reverse


class ObjectContentMixin:
    model: models.Model
    template: str

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj_key = self.model.__name__.lower()
        return render(request, self.template,
                      context={obj_key: obj,
                               'admin_object': obj,
                               'content': True})


class ObjectCreateMixin:
    form_model: 'forms.ModelForm'
    template: str

    def get(self, request: HttpRequest) -> HttpResponse:
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model: models.Model
    form_model: 'forms.ModelForm'
    template: str

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(instance=obj)
        return render(request, self.template,
                      context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template,
                      context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model: models.Model
    template: str
    redirect_url: str

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): obj})

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
