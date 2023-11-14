from django.db import models


class occupation(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ocupacion'
        verbose_name_plural = 'Ocupaciones'
        db_table = 'occupation'
        ordering = ['id']


class worker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    occupation = models.ForeignKey(occupation, on_delete=models.CASCADE)
  
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        db_table = 'Workers'
        ordering = ['id']
        
class typeOfService(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TipoServicio'
        verbose_name_plural = 'TipoServicios'
        db_table = 'typeOfService'
        ordering = ['id']
        
class cite(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    typeOfService = models.ForeignKey(typeOfService, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    worker = models.ForeignKey(worker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.typeOfService.name}"

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        db_table = 'cite'
        ordering = ['id']

class comment(models.Model):
    headLine = models.CharField(max_length=30)
    cite = models.ForeignKey(cite, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.headLine

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        db_table = 'comment'
        ordering = ['id']

class contacts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        db_table = 'contacts'
        ordering = ['id']
      