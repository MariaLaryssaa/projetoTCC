from django.db import models
from django.contrib.postgres.fields import ArrayField

class Autor(models.Model):
    primeiro_nome = models.CharField(max_length=150)
    ultimo_nome = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.primeiro_nome

class Orientador(models.Model):
    primeiro_nome = models.CharField(max_length=150)
    ultimo_nome = models.CharField(max_length=150)
    curriculo = models.URLField()

    def __str__(self):
        return self.primeiro_nome

class Curso(models.Model):
    MODALIDADE = [
        ('B', 'Bacharelado'),
        ('L', 'Licenciatura'),
        ('T', 'Tecnológica'),
    ]
    nome = models.CharField(max_length=50)
    modalidade = models.CharField(max_length=15, choices=MODALIDADE, null=True)

    def __str__(self):
        return self.nome

class TCC(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ano_documento = models.IntegerField(verbose_name="ano do documento")
    resumo = models.TextField()
    arquivo_documento = models.FileField(upload_to='arquivo/')
    palavra_chave = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.titulo

