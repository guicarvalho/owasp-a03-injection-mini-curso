from django.shortcuts import redirect, render

from .models import User


def list_users(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})


def create_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        # Criação de usuário sem sanitização do campo 'name'
        User.objects.create(name=name, phone=phone, email=email)
        return redirect("users:list_users")
    return render(request, "create_user.html")
