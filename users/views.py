from django.shortcuts import render

from .models import User


def search_users(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        # Consulta segura utilizando o ORM do Django
        users = User.objects.filter(name=username)
        return render(request, "user_list.html", {"users": users})
    return render(request, "user_list.html")
