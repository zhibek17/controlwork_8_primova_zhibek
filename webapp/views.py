from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import Review
from .forms import ReviewForm



class ProductListView(ListView):
    model = Product
    template_name = 'product_crud/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_crud/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_crud/product_form.html'
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        return redirect('product_detail', pk=product.pk)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_crud/product_form.html'
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        return redirect('product_detail', pk=product.pk)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_crud/product_delete.html'
    success_url = reverse_lazy('product_list')


class ReviewListView(ListView):
    model = Review
    template_name = 'review_crud/review_list.html'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_crud/review_create.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reviews')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review_crud/review_form.html'
    form_class = ReviewForm

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_staff

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_crud/review_delete.html'
    success_url = reverse_lazy('review_list')

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_staff
