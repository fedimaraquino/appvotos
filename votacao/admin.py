
# Register your models here.
from django.contrib import admin
from .models import Usuario, Candidato, Secao, Cargo, Apurado, Perfil
admin.site.register(Usuario)
admin.site.register(Candidato)
admin.site.register(Secao)
admin.site.register(Cargo)
admin.site.register(Apurado)
admin.site.register(Perfil)