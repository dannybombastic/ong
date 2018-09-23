from django.db import models

# Create your models here.
class Voluntary(models.Model):
  
    id = models.AutoField(primary_key = True, verbose_name= "ID")
    name = models.CharField(max_length = 22, verbose_name= "Name")
    surname = models.CharField(max_length = 22, verbose_name= "Surname")
    address = models.TextField(verbose_name= "Address")
    age = models.IntegerField(blank=True, null=True, verbose_name= "Age")
    tlf = models.CharField(max_length = 22, null=True, verbose_name= "Telephone")
    email = models.EmailField(blank=False, verbose_name= "Email")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creacion')
     
    class Meta:
        verbose_name = "Voluntary"
        verbose_name_plural = "Voluntaries"
        ordering = ['name']

    def __str__(self):
        return '{} {}'.format(self.name,self.surname)

        
class Horarios(models.Model):
    monday = models.BooleanField(default=False, verbose_name="Monday")
    tuesday = models.BooleanField(default=False, verbose_name="Tuesday")
    wednesday = models.BooleanField(default=False, verbose_name="Wednesday")
    thursday = models.BooleanField(default=False, verbose_name="Thursday")
    friday = models.BooleanField(default=False, verbose_name="Friday")
    saturday = models.BooleanField(default=False, verbose_name="Saturday")
    sunday = models.BooleanField(default=False, verbose_name="Sunday")
    fromto = models.CharField(default='07:00', verbose_name="From:", max_length=8)
    to = models.CharField(default='14:00', verbose_name="To:", max_length=8)
    voluntary = models.ManyToManyField(Voluntary, verbose_name="Voluntarios", related_name="get_vol")

    def __str__(self):
        v = self.voluntary.all()
        return '{}'.format(v[0])