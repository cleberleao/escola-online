from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length= 100)
    email = models.EmailField(blank=False, max_length=50)
    cpf = models.CharField(max_length= 11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length= 10)
    descricao = models.CharField(max_length= 100, blank=False)
    nivel = models.CharField(max_length=1, choices= NIVEL, blank=False, default='B')

    def __str__(self):
        return self.codigo

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Manhã'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
        ('O', 'On-Line'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, default='M')