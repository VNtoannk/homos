
from django.shortcuts import render, redirect
from .forms import SiteForm, IP_public_test_Form
from .models import Site, IP_public_test

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
#def resource(request):
#    return render(request, 'resource/resource.html')

def site(request):
    site = Site.objects.all()
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SiteForm()
    context = {
        'site': site,
        'form1': form,
    }
    return render(request, 'resource/resource_ippub.html', context)

def resource_ippub(request):
    return render(request, 'resource/resource_ippub.html')