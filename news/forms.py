from django import forms
from django.core.exceptions import ValidationError

from news.models import Tag, News


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self) -> str:
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'create':
            raise ValidationError('This slug name reserved')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'The slug "{new_slug}" already reserved')
        return new_slug


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'slug', 'body', 'tags', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self) -> str:
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'create':
            raise ValidationError(f'The slug "{new_slug}" already reserved')
        return new_slug
