from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from authapp.models import User
from mainapp.models import Product, ProductCategories
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryUpdateFormAdmin, ProductUpdateFormAdmin
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, TemplateView, CreateView
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'adminapp/admin.html')


class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главная страница'

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     super(IndexTemplateView, self).dispatch(request, *args, **kwargs)
    # def get_context_data(self, **kwargs):
    #     context = super(IndexTemplateView, self).get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     return context


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Админка | Пользователи'
    context_object_name = 'users'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'title': 'Админка | Пользователи',
#         'users': User.objects.all()
#
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')


#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'Админка | Регистрация',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-users-create.html', context)

class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request, id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#         'title': 'Админка | Обновление пользователя',
#         'form': form,
#         'user_select': user_select
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)

class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request, id):
#     user = User.objects.get(id=id).delete()
#     # user.is_active = False
#     # user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))


class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-read.html'
    title = 'Админка | Список категорий'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_category(request):
#     context = {
#         'title': 'Админка | Список категорий',
#         'categories': ProductCategories.objects.all(),
#     }
#     return render(request, 'adminapp/admin-category-read.html', context)

class CategoryCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-create.html'
    form_class = CategoryUpdateFormAdmin
    title = 'Админка | Создание категории'
    success_url = reverse_lazy('adminapp:admin_category')


# def admin_category_create(request):
#     if request.method == 'POST':
#         form = CategoryUpdateFormAdmin(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_category'))
#         else:
#             print(form.errors)
#     else:
#         form = CategoryUpdateFormAdmin()
#     context = {
#         'title': 'Админка | Создание категории',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-category-create.html', context)


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-update-delete.html'
    form_class = CategoryUpdateFormAdmin
    title = 'Админка | Обновление категории'
    success_url = reverse_lazy('adminapp:admin_category')


# def admin_category_update(request, id):
#     category_select = ProductCategories.objects.get(id=id)
#     if request.method == 'POST':
#         form = CategoryUpdateFormAdmin(data=request.POST, instance=category_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_category'))
#     else:
#         form = CategoryUpdateFormAdmin(instance=category_select)
#     context = {
#         'title': 'Админка | Обновление категории',
#         'form': form,
#         'category_select': category_select
#     }
#     return render(request, 'adminapp/admin-category-update-delete.html', context)

class CategoryDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_category')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.product_set.update(is_active=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# def admin_category_delete(request, id):
#     category = ProductCategories.objects.get(id=id).delete()
#     return HttpResponseRedirect(reverse('adminapp:admin_category'))


class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-read.html'
    title = 'Админка | Список продуктов'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product(request):
#     context = {
#         'title': 'Админка | Список продуктов',
#         'products': Product.objects.all(),
#
#     }
#     return render(request, 'adminapp/admin-product-read.html', context)


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-create.html'
    form_class = ProductUpdateFormAdmin
    title = 'Админка | Создание продукта'
    success_url = reverse_lazy('adminapp:admin_product')


# def admin_product_create(request):
#     if request.method == 'POST':
#         form = ProductUpdateFormAdmin(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_product'))
#         else:
#             print(form.errors)
#     else:
#         form = CategoryUpdateFormAdmin()
#     context = {
#         'title': 'Админка | Создание продукта',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-product-create.html', context)


class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-update-delete.html'
    form_class = ProductUpdateFormAdmin
    title = 'Админка | Обновление продукта'
    success_url = reverse_lazy('adminapp:admin_product')


# def admin_product_update(request, id):
#     product_select = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductUpdateFormAdmin(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_product'))
#     else:
#         form = ProductUpdateFormAdmin(instance=product_select)
#     context = {
#         'title': 'Админка | Обновление продукта',
#         'form': form,
#         'product_select': product_select
#     }
#     return render(request, 'adminapp/admin-product-update-delete.html', context)


class ProductDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_product')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# def admin_product_delete(request, id):
#     product = Product.objects.get(id=id).delete()
#     return HttpResponseRedirect(reverse('adminapp:admin_product'))
