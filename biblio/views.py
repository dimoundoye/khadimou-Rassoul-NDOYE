from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Count, Q
from .models import Livre, Emprunt
from .forms import LivreForm, EmpruntForm

class DashboardView(TemplateView):
    template_name = 'biblio/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Livres disponibles : somme des (quantité - emprunts en cours) pour chaque livre
        tous_les_livres = Livre.objects.all()
        total_dispo = sum(l.exemplaires_disponibles for l in tous_les_livres)
        context['livres_disponibles'] = total_dispo
        
        # Auteur le plus productif
        top_auteur = Livre.objects.values('auteur').annotate(nb_livres=Count('id')).order_by('-nb_livres').first()
        context['top_auteur'] = top_auteur
        
        # Quelques stats rapides
        context['total_livres'] = Livre.objects.count()
        context['total_emprunts'] = Emprunt.objects.count()
        return context

# Vues Livre
class LivreListView(ListView):
    model = Livre
    template_name = 'biblio/livre_list.html'
    context_object_name = 'livres'
    paginate_by = 5

class LivreCreateView(CreateView):
    model = Livre
    form_class = LivreForm
    template_name = 'biblio/livre_form.html'
    success_url = reverse_lazy('livre_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tous_les_livres = Livre.objects.all()
        context['livres_disponibles'] = sum(l.exemplaires_disponibles for l in tous_les_livres)
        return context

class LivreUpdateView(UpdateView):
    model = Livre
    form_class = LivreForm
    template_name = 'biblio/livre_form.html'
    success_url = reverse_lazy('livre_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tous_les_livres = Livre.objects.all()
        context['livres_disponibles'] = sum(l.exemplaires_disponibles for l in tous_les_livres)
        return context

class LivreDeleteView(DeleteView):
    model = Livre
    template_name = 'biblio/livre_confirm_delete.html'
    success_url = reverse_lazy('livre_list')

# Vues Emprunt
class EmpruntListView(ListView):
    model = Emprunt
    template_name = 'biblio/emprunt_list.html'
    context_object_name = 'emprunts'
    paginate_by = 5

class EmpruntCreateView(CreateView):
    model = Emprunt
    form_class = EmpruntForm
    template_name = 'biblio/emprunt_form.html'
    success_url = reverse_lazy('emprunt_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tous_les_livres = Livre.objects.all()
        context['livres_disponibles'] = sum(l.exemplaires_disponibles for l in tous_les_livres)
        return context

class EmpruntReturnView(UpdateView):
    model = Emprunt
    fields = ['dateRetour']
    template_name = 'biblio/emprunt_retour.html'
    success_url = reverse_lazy('emprunt_list')
