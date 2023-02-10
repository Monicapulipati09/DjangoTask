from django import forms
from django.conf import settings
from django.contrib import admin
from .forms import ArticlesForm
from .models import Articles


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticlesForm
    list_display = ['Author', 'title_display', 'created', 'updated']
    fieldsets = [
        (None, {'fields': ['Author']}),
        ('Titles', {'fields': [f'title_{lang_code}' for lang_code, lang_name in settings.LANGUAGES]}),

    ]

    def get_form(self, request, obj=None, **kwargs):
        form = ArticlesForm
        form.base_fields['Author'].widget = forms.TextInput()
        return form

    def title_display(self, obj):
        return obj.title.get(settings.LANGUAGE_CODE, "")

    title_display.short_description = "Title"