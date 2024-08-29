
from django.shortcuts import render, get_object_or_404, redirect
from .models import Secao, Usuario, Candidato, Cargo, Apurado
from .forms import SecaoForm, UsuarioForm, CandidatoForm, CargoForm, ApuradoForm
from functools import wraps
from votacao.models import Cargo, Secao, Candidato, Usuario, Perfil, Apurado
from votacao.forms import ApuradoForm
from .decorators import profile_required
from .models import Usuario, Candidato, Secao, Cargo, Apurado
from .forms import ApuradoForm
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.contrib import messages
from django.db import IntegrityError

# Secao Views
def secao_list(request):
    secoes = Secao.objects.all()
    return render(request, 'votacao/secao_list.html', {'secoes': secoes})

def secao_create(request):
    if request.method == 'POST':
        form = SecaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secao_list')
    else:
        form = SecaoForm()
    return render(request, 'votacao/secao_form.html', {'form': form})

def secao_update(request, id):
    secao = get_object_or_404(Secao, id=id)
    if request.method == 'POST':
        form = SecaoForm(request.POST, instance=secao)
        if form.is_valid():
            form.save()
            return redirect('secao_list')
    else:
        form = SecaoForm(instance=secao)
    return render(request, 'votacao/secao_form.html', {'form': form})

def secao_delete(request, id):
    secao = get_object_or_404(Secao, id=id)
    if request.method == 'POST':
        secao.delete()
        return redirect('secao_list')
    return render(request, 'votacao/secao_confirm_delete.html', {'secao': secao})

# Usuario Views
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'votacao/usuario_list.html', {'usuarios': usuarios})



# def usuario_create(request):
#     if request.method == 'POST':
#         form = UsuarioForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Cria o objeto Usuario, mas não salva ainda
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # Crie o usuário do Django e associe ao modelo Usuario
#             user_django = User.objects.create_user(username=username, password=password)
#             user.user = user_django  # Associe o User do Django ao campo user do modelo Usuario
#             user.save()  # Agora salva o objeto Usuario com o user_id preenchido
#             return redirect('usuarios_list')  # Certifique-se de que 'usuarios_list' está mapeado corretamente
#     else:
#         form = UsuarioForm()

#     return render(request, 'votacao/usuario_form.html', {'form': form})

#__________________________________________________________________________________

# def usuario_create(request):
#     if request.method == 'POST':
#         form = UsuarioForm(request.POST)
#         if form.is_valid():
#             try:
#                 # Criação do objeto User
#                 user = User.objects.create_user(
#                     username=form.cleaned_data.get('username'),
#                     password=form.cleaned_data.get('password'),
#                 )
                
#                 # Criação do objeto Usuario e atribuição do user
#                 usuario = form.save(commit=False)
#                 usuario.user = user
#                 usuario.save()
                
#                 return redirect('usuario_list')
#             except IntegrityError:
#                 # Adicione lógica de tratamento para erro de integridade
#                 form.add_error(None, "Erro de integridade, possivelmente nome de usuário duplicado.")
#     else:
#         form = UsuarioForm()

#     return render(request, 'votacao/usuario_form.html', {'form': form})
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'votacao/usuario_form.html', {'form': form})


def usuario_update(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'votacao/usuario_form.html', {'form': form})

def usuario_delete(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'votacao/usuario_confirm_delete.html', {'usuario': usuario})

# Candidato Views
def candidato_list(request):
    candidatos = Candidato.objects.all()
    return render(request, 'votacao/candidato_list.html', {'candidatos': candidatos})

def candidato_create(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('candidato_list')
    else:
        form = CandidatoForm()
    return render(request, 'votacao/candidato_form.html', {'form': form})

def candidato_update(request, id):
    candidato = get_object_or_404(Candidato, id=id)
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('candidato_list')
    else:
        form = CandidatoForm(instance=candidato)
    return render(request, 'votacao/candidato_form.html', {'form': form})

def candidato_delete(request, id):
    candidato = get_object_or_404(Candidato, id=id)
    if request.method == 'POST':
        candidato.delete()
        return redirect('candidato_list')
    return render(request, 'votacao/candidato_confirm_delete.html', {'candidato': candidato})

# Cargo Views
def cargo_list(request):
    cargos = Cargo.objects.all()
    return render(request, 'votacao/cargo_list.html', {'cargos': cargos})

def cargo_create(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo_list')
    else:
        form = CargoForm()
    return render(request, 'votacao/cargo_form.html', {'form': form})

def cargo_update(request, id):
    cargo = get_object_or_404(Cargo, id=id)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargo_list')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'votacao/cargo_form.html', {'form': form})

def cargo_delete(request, id):
    cargo = get_object_or_404(Cargo, id=id)
    if request.method == 'POST':
        cargo.delete()
        return redirect('cargo_list')
    return render(request, 'votacao/cargo_confirm_delete.html', {'cargo': cargo})


#--------------------- Usuarios----------------------------

def profile_required(profile):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.usuario.perfil == profile:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        return _wrapped_view
    return decorator


# @profile_required('fiscal')
# def registrar_resultados(request):
#     secao = request.user.usuario.secao
#     candidatos = Candidato.objects.all()
    
#     if request.method == 'POST':
#         form = ApuradoForm(request.POST)
#         if form.is_valid():
#             apurado = form.save(commit=False)
#             apurado.secao = secao
#             apurado.save()
#             return redirect('resultados_registrados')
#     else:
#         form = ApuradoForm()

#     return render(request, 'votacao/registrar_resultados.html', {'form': form, 'secao': secao, 'candidatos': candidatos})



@profile_required('fiscal')
def registrar_resultados(request):
    secao = request.user.usuario.secao
    candidatos = Candidato.objects.all()

    if request.method == 'POST':
        form = ApuradoForm(request.POST)
        if form.is_valid():
            apurado = form.save(commit=False)
            apurado.secao = secao
            apurado.save()
            return redirect('resultados_registrados')
    else:
        form = ApuradoForm()

    return render(request, 'votacao/registrar_resultados.html', {'form': form, 'secao': secao, 'candidatos': candidatos})

def dashboard(request):
    if request.user.perfil.perfil == 'admin':
        total_cargos = Cargo.objects.count()
        total_secoes = Secao.objects.count()
        total_candidatos = Candidato.objects.count()
        total_usuarios = Usuario.objects.count()

        context = {
            'total_cargos': total_cargos,
            'total_secoes': total_secoes,
            'total_candidatos': total_candidatos,
            'total_usuarios': total_usuarios,
        }

        return render(request, 'votacao/dashboard.html', context)

    elif request.user.perfil.perfil == 'fiscal':
        return redirect('registrar_resultados')

    else:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
# @profile_required('fiscal')
# def registrar_resultados(request):
#     if not hasattr(request.user, 'perfil') or request.user.perfil.perfil != 'fiscal':
#         return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    
#     secao = request.user.perfil.user.secao
#     candidatos = Candidato.objects.all()

#     if request.method == 'POST':
#         form = ApuradoForm(request.POST)
#         if form.is_valid():
#             apurado = form.save(commit=False)
#             apurado.secao = secao
#             apurado.save()
#             return redirect('resultados_registrados')
#     else:
#         form = ApuradoForm()

#     return render(request, 'votacao/registrar_resultados.html', {'form': form, 'secao': secao, 'candidatos': candidatos})



# def dashboard(request):
#     if request.user.usuario.perfil == 'admin':
#         # Exibe o dashboard com os dados agregados
#         total_cargos = Cargo.objects.count()
#         total_secoes = Secao.objects.count()
#         total_candidatos = Candidato.objects.count()
#         total_usuarios = Usuario.objects.count()

#         context = {
#             'total_cargos': total_cargos,
#             'total_secoes': total_secoes,
#             'total_candidatos': total_candidatos,
#             'total_usuarios': total_usuarios,
#         }

#         return render(request, 'votacao/dashboard.html', context)

#     elif request.user.usuario.perfil == 'fiscal':
#         # Redireciona o fiscal para a página de registro de resultados
#         return redirect('registrar_resultados')

#     else:
#         # Retorna um erro 403 se o usuário não tiver permissão
#         return HttpResponseForbidden("Você não tem permissão para acessar esta página.")



# def dashboard(request):
#     if not hasattr(request.user, 'perfil'):
#         return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    
#     if request.user.perfil.perfil == 'admin':
#         # Exibe o dashboard com os dados agregados
#         total_cargos = Cargo.objects.count()
#         total_secoes = Secao.objects.count()
#         total_candidatos = Candidato.objects.count()
#         total_usuarios = Usuario.objects.count()

#         context = {
#             'total_cargos': total_cargos,
#             'total_secoes': total_secoes,
#             'total_candidatos': total_candidatos,
#             'total_usuarios': total_usuarios,
#         }

#         return render(request, 'votacao/dashboard.html', context)

#     elif request.user.perfil.perfil == 'fiscal':
#         # Redireciona o fiscal para a página de registro de resultados
#         return redirect('registrar_resultados')

#     else:
#         # Retorna um erro 403 se o usuário não tiver permissão
#         return HttpResponseForbidden("Você não tem permissão para acessar esta página.")


def resultados_registrados(request):
    # Busca todos os registros de resultados apurados
    resultados = Apurado.objects.all()

    # Passa os resultados para o contexto do template
    context = {
        'resultados': resultados
    }

    # Renderiza o template e passa os resultados
    return render(request, 'votacao/resultados_registrados.html', context)
