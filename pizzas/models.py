from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    #auto_now_add=True - set this attribute to the current date and time
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    #auto_now_add=True - set this attribute to the current date and time
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return self.name