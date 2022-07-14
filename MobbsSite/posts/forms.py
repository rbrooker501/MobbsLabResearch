from socket import fromshare
from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        return title

    def clean(self):
        return self.cleaned_data