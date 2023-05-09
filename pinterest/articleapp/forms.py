from django.forms import fields, ModelForm
from articleapp.models import Article

class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'context']