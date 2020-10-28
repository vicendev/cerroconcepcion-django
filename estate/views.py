from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .models import Estate, EstateImages
from .forms import EstateForm, ImageForm
from .filters import EstateFilter


# Create your views here.

def estate_list(request):
    estates = Estate.objects.all()
    filter = EstateFilter(request.GET, queryset = estates)

    return render(request, "estate/estate_list.html", {'filter': filter})

@login_required
def estate_create(request):

    if request.method == 'POST':
        estateForm = EstateForm(request.POST, request.FILES)
        imageForm = ImageForm(request.POST, request.FILES)

        if estateForm.is_valid() and imageForm.is_valid():
            estate_form = estateForm.save(commit=False)
            estate_form.author = request.user
            estate_form.save()

            for imgs in request.FILES.getlist('file'):
                images = EstateImages(estate=estate_form,file=imgs)
                images.save()

            return redirect(reverse('estates'))
        else:
            print(estateForm.errors , imageForm.errors)
    else:
        estateForm = EstateForm()
        imageForm = ImageForm()
    return render(request,'estate/estate_create.html',{'estateForm':estateForm,'imageForm':imageForm})


def estate_detail(request, pk):
    estate = get_object_or_404(Estate, pk=pk)
    images = EstateImages.objects.filter(estate=pk)
    try:
        selected_estate = Estate.objects.get(pk=pk)
    except (KeyError, Estate.DoesNotExists):
        return render(request, 'estate/estate_detail.html',{'estate':estate,'error_message':'No existe esta publicación',})
    else:
        return render(request, 'estate/estate_detail.html',{'estate':estate,'images':images})

@login_required
def estate_update(request, pk):
    estate = get_object_or_404(Estate, pk=pk)
    images = EstateImages.objects.filter(estate=pk)
    estateForm = EstateForm(request.POST or None, request.FILES or None, instance=estate)
    imageForm = ImageForm(request.POST or None, request.FILES or None, instance=estate)

    if request.POST and estateForm.is_valid() and imageForm.is_valid():
        estate_form = estateForm.save(commit=False)
        estate_form.author = request.user
        estate_form.save()

        if len(request.FILES.getlist('file')) > 0:
            for imgs in request.FILES.getlist('file'):
                images = EstateImages(estate=estate_form,file=imgs)
                images.save()

        return redirect(reverse('estate-detail', args=[pk]))

    return render(request, 'estate/estate_update.html',{'estateForm':estateForm, 'imageForm':imageForm ,'images':images,'pk':pk})


@login_required
def delete_image_update(request):
    pk = request.GET['pk']
    image_to_delete = get_object_or_404(EstateImages, pk=pk)
    image_to_delete.delete()
    return HttpResponse('OK')

def estate_delete(request, pk):
    estate = get_object_or_404(Estate, pk=pk)

    if request.method == 'POST':
        estate.delete()
        return redirect(reverse('estates'))
    
    return render(request, 'estate/estate_delete.html',{'estate':estate})