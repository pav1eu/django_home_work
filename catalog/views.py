from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from catalog.forms import ProductCreateForm
from .services import ProductService
from .models import Product, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponse

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache



class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав на отмену публикации продукта")

        product = get_object_or_404(Product, pk=product_id)
        product.is_published = False
        product.save()
        return redirect('catalog:products_list')

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    permission_required = 'catalog.view_product'

    def get_queryset(self):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'catalog.change_product'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.owner != request.user:
            raise PermissionDenied('Вы не являетесь владельцем данного продукта')
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'catalog.delete_product'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied('Вы не можете удалить этот продукт')
        return super().dispatch(request, *args, **kwargs)


class ProductCategoryView(LoginRequiredMixin, ListView):
    template_name = 'products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return ProductService.get_products_by_category(self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context