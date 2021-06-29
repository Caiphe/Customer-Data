from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now_add=False)
    file = models.FileField(validators=[FileExtensionValidator(['xlsx'])])
    slug = models.SlugField(blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}'
    
    class Meta:
        verbose_name_plural = 'Customers'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.first_name}-{self.last_name}')
        super(Customer, self).save(*args, **kwargs)
