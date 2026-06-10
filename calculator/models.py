from django.db import models


class GravelType(models.Model):
    name = models.CharField(max_length=100)
    density = models.DecimalField(max_digits=5, decimal_places=2, help_text='Density in tons/m³')
    typical_use = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Gravel Type'
        verbose_name_plural = 'Gravel Types'

    def __str__(self):
        return f'{self.name} ({self.density} tons/m³)'
