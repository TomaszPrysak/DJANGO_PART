from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Subcategory
from .forms import PostForm, CategoryForm, SubcategoryForm
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

##########
# Funkcje do pobierania danych

def get_navbar_dict():
    category_list = [(item.name_category, item.slug_category) for item in Category.objects.all()]
    navbarDict = {}

    for item in category_list:
        if item not in navbarDict:
            navbarDict[item] = []

    for subcategory in Subcategory.objects.all():
        for key, value in navbarDict.items():
            if str(subcategory.main_category) == key[0]:
                navbarDict[key].append((subcategory.name_subcategory, subcategory.slug_subcategory))

    return navbarDict

# Funkcje do pobierania danych
##########

##########
# Funkcje widoków

# Wyświetlanie wszystkich postów z wszystkich kategorii
# Podzielonych na 5 na stronie
# Tekst postu ograniczony do 300 znaków
def all_post_list(request):
    navbarDict = get_navbar_dict()
    allPostList = Post.objects.all()
    paginator = Paginator(allPostList, 5)

    page_number = request.GET.get('page')
    postListDict = paginator.get_page(page_number)

    pageData = {
        'navbarDict':navbarDict,
        'postListDict':postListDict
    }
    return render(request, 'blog/post_list.html', pageData)

# Wyświetlanie postów należących do głównej kategorii. Czyli tych należących do modelu danych "Category"
# Podzielonych na 5 na stronie
# Tekst postu ograniczony do 300 znaków
def category_post_list(request, slug_category):
    navbarDict = get_navbar_dict()
    filteredCategoryPostList = Post.objects.filter(category__slug_category=slug_category)
    paginator = Paginator(filteredCategoryPostList, 5)

    page_number = request.GET.get('page')
    postListDict = paginator.get_page(page_number)

    pageData = {
        'navbarDict':navbarDict,
        'postListDict':postListDict
    }
    return render(request, 'blog/post_list.html', pageData)

# Wyświetlanie postów należących do podkategorii. Czyli tych należących do modelu danych "Subcategory"
# Podzielonych na 5 na stronie
# Tekst postu ograniczony do 300 znaków
def subcategory_post_list(request, slug_subcategory):
    navbarDict = get_navbar_dict()
    filteredSubcategoryPostList = Post.objects.filter(subcategory__slug_subcategory=slug_subcategory)
    paginator = Paginator(filteredSubcategoryPostList, 5)

    page_number = request.GET.get('page')
    postListDict = paginator.get_page(page_number)

    pageData = {
        'navbarDict':navbarDict,
        'postListDict':postListDict
    }
    return render(request, 'blog/post_list.html', pageData)

# Wyświetlenie jednego postu na stronie
def post_detail(request, slug):
    navbarDict = get_navbar_dict()
    postDetailDict = Post.objects.get(slug=slug)

    pageData = {
        'navbarDict':navbarDict,
        'postDetailDict':postDetailDict
    }
    return render(request, 'blog/post_detail.html', pageData)

# Widok logowanie użytkownika
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('blog:succes_login'))
            else:
                return HttpResponseRedirect(reverse('blog:failed_login'))
        else:
            return HttpResponseRedirect(reverse('blog:failed_login'))

    else:
        navbarDict = get_navbar_dict()
        pageData = {
            'navbarDict':navbarDict,
        }
        return render(request, 'blog/login.html', pageData)

# Widok po poprawnym zalogowaniu
@login_required
def succes_login(request):
    navbarDict = get_navbar_dict()
    pageData = {
        'navbarDict':navbarDict,
    }
    return render(request, 'blog/succes_login.html', pageData)

# Widok po niepoprawnym logowaniu
def failed_login(request):
    navbarDict = get_navbar_dict()
    pageData = {
        'navbarDict':navbarDict,
    }
    return render(request, 'blog/failed_login.html', pageData)

# Wylogowanie użytkownika
@login_required
def user_logut(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:succes_logout'))

# Widok po poprawnym wylogowaniu
def succes_logout(request):
    navbarDict = get_navbar_dict()
    pageData = {
        'navbarDict':navbarDict,
    }
    return render(request, 'blog/succes_logout.html', pageData)

@login_required
def new_post_form(request):
    form = PostForm()
    navbarDict = get_navbar_dict()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            form.save(commit=True)
            return post_add_succes(request, post_title)
        else:
            print("Błąd podczas walidacji danych z formularza")
    pageData = {
        'navbarDict':navbarDict,
        'form':form,
    }
    return render(request, 'blog/post_form.html', pageData)

# Widok po sukcesie dodawania postu
@login_required
def post_add_succes(request, post_title):
    navbarDict = get_navbar_dict()
    post_title = post_title
    pageData = {
        'navbarDict':navbarDict,
        'post_title':post_title,
    }
    return render(request, 'blog/post_add_succes.html', pageData)

# Wydok do usuwania postu
@login_required
def post_remove(request, slug):
    navbarDict = get_navbar_dict()
    post = get_object_or_404(Post, slug=slug)
    if request.method =="POST":
        post_title = post.title
        post.delete()
        return post_remove_succes(request, post_title)
    pageData = {
        'navbarDict':navbarDict,
        'post':post
    }
    return render(request, 'blog/post_confirm_delete.html', pageData)

# Widok po usunięciu postu
@login_required
def post_remove_succes(request, post_title):
    navbarDict = get_navbar_dict()
    post_title = post_title
    pageData = {
        'navbarDict':navbarDict,
        'post_title':post_title,
    }
    return render(request, 'blog/post_remove_succes.html', pageData)

# Widok dodawania nowej kategorii głównej
@login_required
def new_category_form(request):
    form = CategoryForm()
    navbarDict = get_navbar_dict()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['name_category']
            form.save(commit=True)
            return category_add_succes(request, category_name)
        else:
            print("Błąd podczas walidacji danych z formularza")
    pageData = {
        'navbarDict':navbarDict,
        'form':form,
    }
    return render(request, 'blog/category_form.html', pageData)

# Widok po sukcesie dodawania kategorii głównej
@login_required
def category_add_succes(request, category_name):
    navbarDict = get_navbar_dict()
    category_name = category_name
    pageData = {
        'navbarDict':navbarDict,
        'category_name':category_name,
    }
    return render(request, 'blog/category_add_succes.html', pageData)

# Wydok do usuwania kategorii głównej
@login_required
def category_remove(request, slug_category):
    navbarDict = get_navbar_dict()
    category = get_object_or_404(Category, slug_category=slug_category)
    if request.method =="POST":
        category_name = category.name_category
        category.delete()
        return category_remove_succes(request, category_name)
    pageData = {
        'navbarDict':navbarDict,
        'category':category
    }
    return render(request, 'blog/category_confirm_delete.html', pageData)

# Widok po usunięciu kategorii głównej
@login_required
def category_remove_succes(request, category_name):
    navbarDict = get_navbar_dict()
    category_name = category_name
    pageData = {
        'navbarDict':navbarDict,
        'category_name':category_name,
    }
    return render(request, 'blog/category_remove_succes.html', pageData)

# Widok dodawania nowej podkategorii
@login_required
def new_subcategory_form(request):
    form = SubcategoryForm()
    navbarDict = get_navbar_dict()
    if request.method == "POST":
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            subcategory_name = form.cleaned_data['name_subcategory']
            form.save(commit=True)
            return subcategory_add_succes(request, subcategory_name)
        else:
            print("Błąd podczas walidacji danych z formularza")
    pageData = {
        'navbarDict':navbarDict,
        'form':form,
    }
    return render(request, 'blog/subcategory_form.html', pageData)

# Widok po sukcesie dodawania podkategorii
@login_required
def subcategory_add_succes(request, subcategory_name):
    navbarDict = get_navbar_dict()
    subcategory_name = subcategory_name
    pageData = {
        'navbarDict':navbarDict,
        'subcategory_name':subcategory_name,
    }
    return render(request, 'blog/subcategory_add_succes.html', pageData)

# Wydok do usuwania podkategorii
@login_required
def subcategory_remove(request, slug_subcategory):
    navbarDict = get_navbar_dict()
    subcategory = get_object_or_404(Subcategory, slug_subcategory=slug_subcategory)
    if request.method =="POST":
        subcategory_name = subcategory.name_subcategory
        subcategory.delete()
        return subcategory_remove_succes(request, subcategory_name)
    pageData = {
        'navbarDict':navbarDict,
        'subcategory':subcategory
    }
    return render(request, 'blog/subcategory_confirm_delete.html', pageData)

# Widok po usunięciu podkategorii
@login_required
def subcategory_remove_succes(request, subcategory_name):
    navbarDict = get_navbar_dict()
    subcategory_name = subcategory_name
    pageData = {
        'navbarDict':navbarDict,
        'subcategory_name':subcategory_name,
    }
    return render(request, 'blog/subcategory_remove_succes.html', pageData)

# Funkcje widoków
##########
