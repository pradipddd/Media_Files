from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document


def Home_view(request):
    template_name='home.html'
    context={}
    return render(request,template_name,context)


def model_form_upload(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_upload')
    template_name='model_form_upload.html'
    context={'form':form}
    return render(request,template_name,context)

def show_upload_view(request):
    file=Document.objects.all()
    template_name='show_uplaod.html'
    context={'file':file}
    return render(request,template_name,context)
