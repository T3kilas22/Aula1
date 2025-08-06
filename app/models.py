from django.db import models

# Create your models here.
class Agenda(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome} - {self.telefone}'

    @classmethod
    def novo(cls, nome, telefone):
        return cls.objects.create(nome=nome, telefone=telefone)
    
    @classmethod
    def deletar(cls, id):
            cls.objects.filter(id=id).delete()

    @classmethod
    def listar(cls):
        return cls.objects.all()