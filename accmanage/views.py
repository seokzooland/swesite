from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Accinfo
from django.shortcuts import render
from django.contrib import messages


def index(request):
    acc_list = Accinfo.objects.order_by('name')
    context = {'acc_list': acc_list}

    return render(request, 'accmanage/acc_list.html', context)


def acc_delete(request, acc_id):
    acc = Accinfo.objects.get(id=acc_id)
    acc.delete()
    return redirect('accmanage:index')