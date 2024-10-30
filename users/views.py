import bleach
from django.shortcuts import redirect, render

from .models import User


def list_users(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})


def create_user(request):
    if request.method == "POST":
        # Sanitiza os campos para remover scripts ou tags perigosas
        name = bleach.clean(request.POST.get("name"), tags=[], strip=True)
        phone = bleach.clean(request.POST.get("phone"), tags=[], strip=True)
        email = bleach.clean(request.POST.get("email"), tags=[], strip=True)

        # Criação de usuário sem sanitização do campo 'name'
        User.objects.create(name=name, phone=phone, email=email)
        return redirect("users:list_users")
    return render(request, "create_user.html")
