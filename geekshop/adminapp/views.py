from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from authapp.models import User
from mainapp.models import Product, ProductCategories
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryUpdateFormAdmin, ProductUpdateFormAdmin


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'Админка | Пользователи',
        'users': User.objects.all()

    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Админка | Регистрация',
        'form': form
    }
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Админка | Обновление пользователя',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id).delete()
    # user.is_active = False
    # user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
    context = {
        'title': 'Админка | Список категорий',
        'categories': ProductCategories.objects.all(),

    }
    return render(request, 'adminapp/admin-category-read.html', context)


def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryUpdateFormAdmin(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_category'))
        else:
            print(form.errors)
    else:
        form = CategoryUpdateFormAdmin()
    context = {
        'title': 'Админка | Создание категории',
        'form': form
    }
    return render(request, 'adminapp/admin-category-create.html', context)


def admin_category_update(request, id):
    category_select = ProductCategories.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryUpdateFormAdmin(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_category'))
    else:
        form = CategoryUpdateFormAdmin(instance=category_select)
    context = {
        'title': 'Админка | Обновление категории',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'adminapp/admin-category-update-delete.html', context)


def admin_category_delete(request, id):
    category = ProductCategories.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('adminapp:admin_category'))


@user_passes_test(lambda u: u.is_superuser)
def admin_product(request):
    context = {
        'title': 'Админка | Список продуктов',
        'products': Product.objects.all(),

    }
    return render(request, 'adminapp/admin-product-read.html', context)


def admin_product_create(request):
    if request.method == 'POST':
        form = ProductUpdateFormAdmin(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_product'))
        else:
            print(form.errors)
    else:
        form = CategoryUpdateFormAdmin()
    context = {
        'title': 'Админка | Создание продукта',
        'form': form
    }
    return render(request, 'adminapp/admin-product-create.html', context)



def admin_product_update(request, id):
    product_select = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductUpdateFormAdmin(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_product'))
    else:
        form = ProductUpdateFormAdmin(instance=product_select)
    context = {
        'title': 'Админка | Обновление продукта',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'adminapp/admin-product-update-delete.html', context)



def admin_product_delete(request, id):
    product = Product.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('adminapp:admin_product'))