from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib import messages

def home_page(request):                                 #gallery
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, "photos/home_page.html", context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    description = Photo.objects.get(id=pk)
    context = {"photo": photo, "description": description}
    return render(request, 'photos/view_photo.html', context)

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('home_page',)

    context = {'categories': categories}
    return render(request, 'photos/add_photo.html', context)

def delete_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == "POST":
        photo.delete()
        messages.success(request, ("It's been deleted."))
        return redirect("home_page")
    return render(request, "photos/del_photo.html", {"photo": photo})