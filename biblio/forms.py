from django import forms
from .models import Livre, Emprunt

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'isbn', 'quantite']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du livre'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'auteur"}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN (13 chiffres)'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['livre', 'dateRetour']
        widgets = {
            'livre': forms.Select(attrs={'class': 'form-select'}),
            'dateRetour': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrer pour ne montrer que les livres qui ont encore des exemplaires disponibles
        tous_les_livres = Livre.objects.all()
        ids_disponibles = [l.id for l in tous_les_livres if l.exemplaires_disponibles > 0]
        self.fields['livre'].queryset = Livre.objects.filter(id__in=ids_disponibles)
