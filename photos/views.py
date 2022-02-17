from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import DetailView , DeleteView
from django.contrib import messages
# Create your views here.

def about(request):
    return render(request,'photos/about.html')

def index(request):
    category = request.GET.get('category')
    if category == None:
        photo = Photo.objects.all()
    else:
        photo = Photo.objects.filter(category__name=category)
    
    cat=Category.objects.all()
   

    
    return render(request,'photos/gallery.html',{'photos':photo,'categories':cat})

def addphoto(request):
    if request.method == 'POST':
        data = request.POST
        desc= request.POST['description']
        image = request.FILES['images']


        if data['category'] != None:
            category = Category.objects.get(id=data['category'])
        else:
            category = None
    
        a =Photo(desc=desc,category=category,image=image)
        a.save()
        return redirect('home')
    categories = Category.objects.all()
    return render(request,'photos/add.html',{'cat':categories})

class photodetail(DetailView):
    model = Photo
    template_name = 'photos/photo.html'
    

class DelePhoto(DeleteView):
    model = Photo
    template_name = 'photos/confirm_delete.html'
    success_url = reverse_lazy('home')

def delete(request,pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    messages.success(request,'photo delete succesfully')
    return redirect('home')


def search(request):
    pass