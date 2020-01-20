from django.db import models
from django.urls import reverse_lazy


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images', verbose_name="Imagem", null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    update_at = models.DateTimeField("Atualizado em ", auto_now=True)
    objects = CourseManager()

    # customizando para o django admin
    def __str__(self):
        return self.name
    # também customizando o django admin

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse_lazy('details', kwargs={'slug': self.slug})