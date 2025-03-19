from django.db import models

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='static/', null=True, blank=True)  # Champ pour la vidéo
    date_creation = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add= True)
    image = models.ImageField(upload_to='blogs', null= True , blank = True)

    def __str__(self):
        return self.titre
