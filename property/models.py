from django.db import models

# Create your models here.
categories=(
    ("cement","cement"),
    ("rods","rods"),
    ("others","others"),  
)

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=30,null=True)
    message=models.TextField()


    def __str__(self):
        show=self.email

        if self.email:
            show
        else:
            show=self.name
        return show
    
class Products(models.Model):
    Category=models.CharField(max_length=100,choices=categories)
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.ImageField(upload_to="product_images")
    description=models.CharField(max_length=100)
    

class Newsletter(models.Model):
    email=models.EmailField()


class Work(models.Model):
    place=models.CharField(max_length=100)
    discription=models.TextField()
    image=models.ImageField(upload_to="works")


class Pictures(models.Model):
    work=models.ForeignKey(Work,on_delete=models.CASCADE)
    images=models.ImageField(upload_to="works")