from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.form01.forms import UserForm


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # 如果数据验证成功
        if form.is_valid():
            # 相当于 request.POST.get('name')
            name = form.cleaned_data['name']
            # 相当于 request.POST.get('password')
            password = form.cleaned_data['password']
            is_read = form.cleaned_data['is_read']
            image = form.cleaned_data['image']
            print(name)
            print(password)
            print(is_read)
            return HttpResponse('11111')
    else:
        form = UserForm()
    return render(request, 'form01.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # 如果数据验证成功
        if form.is_valid():
            form.save()
            return HttpResponse('11111')
    else:
        form = UserForm()
    return render(request, 'form01.html', {'form': form})



