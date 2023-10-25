from django.shortcuts import render, redirect
from .models import User,Group
from .forms import UserForm, GroupForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    users = User.objects.all()
    return render(request,'main/index.html',{'users': users} )


def groups(request):
    group = Group.objects.all()
    return render(request, 'main/groups.html', {'group': group})

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'main/create_user.html',{'form': form} )

@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('/')
    else:
        formG = GroupForm()

    return render(request, 'main/create_group.html', {'form': formG})

@csrf_exempt
def edit_user(request,id):
    user = User.objects.get(id=id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.group = request.POST.get("group")
        user.save()
        return redirect("/")
    else:
        return render(request, "main/edit_user.html", {"user": user})

@csrf_exempt
def delete_user(request,id):
    person = User.objects.get(id=id)
    person.delete()
    return redirect("/")


def edit_group(request,id):
    group = Group.objects.get(id=id)

    if request.method == "POST":
        group.name = request.POST.get("name")
        group.description = request.POST.get("description")
        group.save()
        return redirect("")
    else:
        return render(request, "edit.html", {"group": group})


@csrf_exempt
def delete_group(request, id):
    group = Group.objects.get(id=id)
    group.delete()
    return redirect("/")