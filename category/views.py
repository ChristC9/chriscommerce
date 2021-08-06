from django.shortcuts import render,redirect
from .models import AllCategories,SubCategories
from .forms import SubCategoryForm
from django.contrib.auth.decorators import login_required
from .decorators import allow_user
# Create your views here.
def Category(request):
    context={
        'title':"All Categories",
        'cats':AllCategories.objects.all()
    }
    return render(request,'category/cat.html',context)

@login_required
@allow_user(allow_roles=['admins'])
def SubCategory(request):
    context={
        'title':"Sub-Categories",
        'subcats':SubCategories.objects.all()
    }
    return render(request,'category/sub.html',context)

def Create(request):
   
    if request.method=='POST':
        form=SubCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cat/sub/')
    else:
       form=SubCategoryForm() 

    return render(request,'category/create.html',{'form':form})

def Delete(request,id):
    subcategory=SubCategories.objects.get(pk=id)
    subcategory.delete()
    return redirect('/cat/sub/')

def Update(request,id):
    subcategory=SubCategories.objects.get(pk=id)
    if request.method=='POST':
        form=SubCategoryForm(request.POST,request.FILES,instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('/cat/sub/')
    else:
        form=SubCategoryForm(instance=subcategory)   
    return render(request,'category/edit.html',{'form':form})    

