from django.shortcuts import render
from django.urls import reverse
from commentapp.models import Comment
from commentapp.forms import CommentCreationForm
from articleapp.models import Article
from django.views.generic import CreateView
# Create your views here.


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    
    def form_valid(self, form):
        temp_commment = form.save(commit=False)
        temp_commment.article = Article.objects.get(pk = self.request.POST['article_pk'])
        temp_commment.writer = self.request.user
        temp_commment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})