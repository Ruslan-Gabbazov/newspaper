from django.db import models
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render


class ObjectContentMixin:
    model: models.Model = None
    template: str = None

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj_key = self.model.__name__.lower()
        return render(request, self.template, context={obj_key: obj})
