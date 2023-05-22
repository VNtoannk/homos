from django.shortcuts import render, redirect
from .models import CountryData, TaskDue
from .forms import CountryDataFrom, TaskForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required(login_url='login')
def index(request):
    data= CountryData.objects.all()
    if request.method =='POST':
        form = CountryDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CountryDataFrom()
    context={
        'data': data,
        'form' : form,
    }
    return render(request, 'dashboard/index.html',context)

@login_required(login_url='login')
def taskdue(request):
    obj = TaskDue.objects.all().values().order_by('-number')
    form1 = TaskForm(request.POST or None)
    
    if form1.is_valid():
        form1.save()
        messages.success(request,'Bạn đã nhập thành công!')
        return redirect(taskdue)
       
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 10)
    try:
        objp=paginator.page(page)
    except PageNotAnInteger:
        objp=paginator.page(1)
    except EmptyPage:
        objp=paginator.page(paginator.num_pages)

    cont ={
        'members':objp,
        'formtask': form1
    }
    return render(request, 'resource/duetask.html', cont)