from django.urls import path
from myblog.views import BlogDetailView, BlogListView, BlogDeleteView, BlogUpdateView, BlogCreateView

app_name = 'myblog'

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs_list'),
    path('blogs/new/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
