# contact_app/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactManualForm, ContactModelForm
from .models import Contact

def contact_manual(request):
    if request.method == 'POST':
        form = ContactManualForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, "Message sent successfully!")
            return redirect('contact_manual')
        else:
            messages.error(request, "There were errors. Please fix them.")
    else:
        form = ContactManualForm()
    return render(request, 'contact_manual.html', {'form': form})

def contact_modelform(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('contact_modelform')
        else:
            messages.error(request, "There were errors. Please fix them.")
    else:
        form = ContactModelForm()
    return render(request, 'contact_modelform.html', {'form': form})
