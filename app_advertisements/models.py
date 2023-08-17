from django.db import models


class Advertisement(models.Model):

    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
    auction = models.BooleanField('Запрос скидки', help_text='Отметьте, если скдидки возможны')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    class Meta:
        db_table = 'advertisements'

