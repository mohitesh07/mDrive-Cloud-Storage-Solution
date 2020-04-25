from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UploadDataForm
from .models import UploadDataset
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib.sites.models import Site
import os

@login_required(login_url='login')
def Download(request, id):
    if (UploadDataset.objects.filter(id=id)[0].user == request.user) or UploadDataset.objects.filter(id=id)[0].share :
        path = str(UploadDataset.objects.filter(id=id)[0])
        file_path = os.path.join(settings.MEDIA_ROOT,path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(
                    fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = 'inline; filename=' + \
                    os.path.basename(file_path)
                return response
    else:
        raise Http404

def Share(request, id):
    if UploadDataset.objects.filter(id=id)[0].user == request.user:
        UploadDataset.objects.filter(id=id).update(share=True)
        current_site = Site.objects.get_current()
        domain = current_site.domain
        return redirect('dashboard')
    else:
        raise Http404

@login_required(login_url='login')
def OffShare(request, id):
    if UploadDataset.objects.filter(id=id)[0].user == request.user:
        UploadDataset.objects.filter(id=id).update(share=False)
        return redirect('dashboard')
    else:
        raise Http404

@login_required(login_url='login')
def DataDelete(request, path):
    UploadDataset.objects.filter(id=path).delete()
    return redirect('dashboard')


@login_required(login_url='login')
def DataUpload(request):
    form = UploadDataForm()
    if request.method == 'POST' and request.FILES['file_in_memory']:
        form = UploadDataForm(request.POST, request.FILES)
        file_size = request.FILES['file_in_memory'].size
        if form.is_valid() and (file_size<=settings.MAX_UPLOAD_SIZE):
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'File '+request.FILES['file_in_memory'].name +
                             ' was uploaded successfully.')
            return redirect('dataUpload')
        else:
            messages.warning(
                request, 'UPLOAD ERROR: Maximum file size allowed is '+str(settings.MAX_UPLOAD_SIZE) + 'bytes')
            return redirect('dataUpload')

    CONTEXT = {
        'form': form,
    }
    return render(request, 'main/upload_file.html', CONTEXT)

def Home(request):
    return render(request, 'main/home.html')

@login_required(login_url='login')
def Dashboard(request):
    datasets = list(UploadDataset.objects.filter(
        user=request.user).values().order_by('-created_at'))
    current_site = Site.objects.get_current()
    domain = current_site.domain
    CONTEXT = {
        'datasets': datasets,
        'domain':domain,
    }
    return render(request, 'main/dashboard.html', CONTEXT)
