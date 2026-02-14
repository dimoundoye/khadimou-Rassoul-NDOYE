from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    quantite = models.PositiveIntegerField(default=1, verbose_name="Nombre d'exemplaires")

    def __str__(self):
        return self.titre

    @property
    def exemplaires_empruntes(self):
        return self.emprunts.filter(dateRetour__isnull=True).count()

    @property
    def exemplaires_disponibles(self):
        return max(0, self.quantite - self.exemplaires_empruntes)

    @property
    def est_disponible(self):
        return self.exemplaires_disponibles > 0

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='emprunts')
    dateEmprunt = models.DateField(auto_now_add=True)
    dateRetour = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.livre.titre} emprunté le {self.dateEmprunt}"
