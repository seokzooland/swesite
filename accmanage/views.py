from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from common.forms import UserForm
from django.contrib.auth.models import User


def index(request):
    acc_list = User.objects.order_by('id')
    context = {'acc_list': acc_list}

    return render(request, 'accmanage/acc_list.html', context)


def acc_delete(request, acc_id):
    acc = User.objects.get(id=acc_id)
    acc.delete()
    return redirect('accmanage:index')