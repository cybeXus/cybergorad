from django.db import models

class Formation_dev_web(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='static/dev_web', null=True, blank=True)  # Champ pour la vidéo
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre
        

class Formation_cybersecurite(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='static/cybersecurite', null=True, blank=True)  # Champ pour la vidéo
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre


class Formation_reseau(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()    
    video = models.FileField(upload_to='static/reseau', null=True, blank=True)  # Champ pour la vidéo
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre


class Formation_dev_mobile(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='static/dev_mobile', null=True, blank=True)  # Champ pour la vidéo
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre


class Formation_design(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='static/design', null=True, blank=True)  # Champ pour la vidéo
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre

        


class Blog(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add= True)
    image = models.ImageField(upload_to='blogs', null= True , blank = True)

    def __str__(self):
        return self.titre
