from django import forms
from .models import Secao, Usuario, Candidato, Cargo, Apurado

class SecaoForm(forms.ModelForm):
    class Meta:
        model = Secao
        fields = ['local', 'numero']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'secao', 'perfil']

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'numero', 'foto', 'partido', 'cargo']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['cargo']

class ApuradoForm(forms.ModelForm):
    class Meta:
        model = Apurado
        fields = ['secao', 'candidato', 'cargo', 'votos_validos', 'votos_branco', 'votos_nulos', 'foto']
