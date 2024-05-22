from django.db import models


class cliente (models.Model):
    nome = models.CharField(max_length=50)
    sobreNome = models.CharField(max_length=50)

    def _str_(self):
        return self.nome
        return self.sobreNome
