from django.conf import settings
from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):
    """
    Custom form for Article model. Dynamically generates fields for each language specified in LANGUAGES setting.
    """

    class Meta:
        model = Articles
        fields = ('Author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for lang_code, lang_name in settings.LANGUAGES:
            self.fields[f'title_{lang_code}'] = forms.CharField(label=f'Title ({lang_name})', required=lang_code == settings.LANGUAGE_CODE)
            if self.instance.pk:
                self.initial[f'title_{lang_code}'] = self.instance.title.get(lang_code, '')

    def save(self, commit=True):
        article = super().save(commit=False)
        article.title = {lang_code: self.cleaned_data[f'title_{lang_code}'] for lang_code, lang_name in settings.LANGUAGES}
        if commit:
            article.save()
        return article