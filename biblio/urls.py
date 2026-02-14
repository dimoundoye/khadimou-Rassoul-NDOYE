from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('livres/', views.LivreListView.as_view(), name='livre_list'),
    path('livres/ajouter/', views.LivreCreateView.as_view(), name='livre_create'),
    path('livres/<int:pk>/modifier/', views.LivreUpdateView.as_view(), name='livre_update'),
    path('livres/<int:pk>/supprimer/', views.LivreDeleteView.as_view(), name='livre_delete'),
    path('emprunts/', views.EmpruntListView.as_view(), name='emprunt_list'),
    path('emprunts/ajouter/', views.EmpruntCreateView.as_view(), name='emprunt_create'),
    path('emprunts/<int:pk>/retour/', views.EmpruntReturnView.as_view(), name='emprunt_return'),
]
