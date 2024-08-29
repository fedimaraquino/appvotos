
# Register your models here.
from django.contrib import admin
from .models import Usuario, Candidato, Secao, Cargo, Apurado, Perfil
from django.contrib import admin
from django.contrib.auth.models import User
from votacao.models import Usuario, Secao

#admin.site.register(Usuario)
admin.site.register(Candidato)
admin.site.register(Secao)
admin.site.register(Cargo)
admin.site.register(Apurado)
admin.site.register(Perfil)

class UsuarioAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na lista do Django Admin
    list_display = ('id', 'user', 'nome', 'secao', 'perfil')
    # Permite a edição direta desses campos na lista do Django Admin
   # list_editable = ('nome', 'secao', 'perfil')
    # Adiciona campos de busca no Django Admin
    search_fields = ('nome', 'user__username')
    # Adiciona filtros laterais no Django Admin
    list_filter = ('secao', 'perfil')

# Registra o model Usuario com a customização do UsuarioAdmin
admin.site.register(Usuario, UsuarioAdmin)

# class UsuarioAdmin(admin.ModelAdmin):
#     try:
#         secao = Secao.objects.first()
#         admin_user = User.objects.get(username='admin')

#         if not hasattr(admin_user, 'usuario'):
#             Usuario.objects.create(user=admin_user, secao=secao, perfil='admin')
#     except Exception as e:
#         pass  # ou logar o erro

# admin.site.register(Usuario, UsuarioAdmin)
# @admin.register(Usuario)
# class UsuarioAdmin(admin.ModelAdmin):
#     list_display = ('user', 'secao', 'perfil')
#     search_fields = ('user__username', 'secao__numero', 'perfil')