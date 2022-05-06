from django.db import models

class product(models.Model):
  name = models.CharField(max_length=100)
  category_name= models.CharField(max_length=100)
  descreption = models.CharField(max_length=100)
  buy_price = models.IntegerField()
  sell_price = models.IntegerField()
  quantity = models.IntegerField()

  def __str__(self):
    return self.name
