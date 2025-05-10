from django.urls import reverse_lazy, reverse

from .models import Blog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('myblog:blogs_list')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object



class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('myblog:blogs_list')

    def get_success_url(self):
        return reverse('myblog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('myblog:blogs_list')
