from django import forms
from django.core.exceptions import ValidationError

from news.models import Tag


class TagForm(forms.Form):
    title = forms.CharField(max_length=150)
    slug = forms.CharField(max_length=150)

    def clean_slug(self) -> str:
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'create':
            raise ValidationError('This slug name reserved')
        return new_slug

    def save(self) -> Tag:
        new_tag = Tag.objects.create(**self.cleaned_data)
        return new_tag
