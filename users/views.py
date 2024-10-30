from django.db import connection
from django.shortcuts import render


def search_users(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        # Consulta SQL direta (não protegida contra SQL Injection)
        query = f"SELECT * FROM users_user WHERE name = '{username}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return render(request, "user_list.html", {"users": result})
    return render(request, "user_list.html")
