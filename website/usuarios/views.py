from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.urls import reverse

Usuario = get_user_model()

def cadastrar_usuario(request):
    erro = None
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        avatar_img = request.FILES.get("avatar")  # pega o arquivo
        bio = request.POST.get("bio")
        data_nascimento = request.POST.get('data')

        # validações manuais
        if not username or not email or not password1:
            erro = "Preencha todos os campos."
        elif password1 != password2:
            erro = "As senhas não conferem."
        elif Usuario.objects.filter(username=username).exists():
            erro = "Esse nome de usuário já existe."
        else:
            # cria o usuário
            user = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password1,
                avatar =  avatar_img if avatar_img else "" ,                
                bio=bio,
                data_nascimento=data_nascimento
            )

            
            user.save()

            login(request, user)
            return redirect('home_area_restrita')

    return render(request, "cadastro.html", {"erro": erro})


def login_usuario(request):
    erro = None
    if request.method == "POST":
        nome = request.POST.get("username")
        senha = request.POST.get("password")
        user = authenticate(request, username=nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect("home_area_restrita")
        else:
            erro = "Usuário ou senha inválidos."
            return render(request, "login.html", {"erro": erro})
    return render(request, "login.html")



def logout_usuario(request):
    request.session.flush()
    return redirect(reverse('home'))
 


# @login_required
# def area_restrita(request):
#     return render(request, "area_restrita.html")