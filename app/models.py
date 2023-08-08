from django.core.validators import RegexValidator
from django.db import models


class Product_Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,verbose_name="Mahsulot nomi")
    price = models.IntegerField(verbose_name="Mahsulot narxi")
    info = models.TextField(verbose_name="Mahsulot haqida")
    descriptions = models.TextField(verbose_name='Mahsulot tavsifi')
    image_1 = models.FileField(upload_to='image/',verbose_name='Mahsulot 1 chi rasmi')
    image_2 = models.FileField(upload_to='image/',verbose_name='Mahsulot 2 chi rasmi',blank=True,null=True)
    image_3 = models.FileField(upload_to='image/',verbose_name='Mahsulot 3 chi rasmi',blank=True,null=True)
    image_4 = models.FileField(upload_to='image/',verbose_name='Mahsulot 4 chi rasmi',blank=True,null=True)
    characteristic = models.TextField(verbose_name='Mahsulot xarakteri')


    def __str__(self):
        return self.title


class Project_Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Project(models.Model):
    category = models.ForeignKey(Project_Category,on_delete=models.CASCADE,verbose_name="Loyihaning Kategoriyasi")
    title = models.CharField(max_length=50,verbose_name="Loyiha nomi")
    descriptions = models.TextField(verbose_name="Loyiha tavsifi")
    power = models.CharField(max_length=40,verbose_name="Loyiha quvvati")
    annual_productivity = models.CharField(max_length=40,verbose_name="Yillik hosildorlik")
    amount_of_savings = models.IntegerField(verbose_name="Tejamkorlik miqdori")
    image_1 = models.ImageField(upload_to="project/images/")
    image_2 = models.ImageField(upload_to="project/images/",blank=True,null=True)
    image_3 = models.ImageField(upload_to="project/images/",blank=True,null=True)
    image_4 = models.ImageField(upload_to="project/images/",blank=True,null=True)
    image_5 = models.ImageField(upload_to="project/images/",blank=True,null=True)
    image_6 = models.ImageField(upload_to="project/images/",blank=True,null=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=250,verbose_name="Blogning nomi")
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/images/',verbose_name='Blogning rasmi')
    description = models.TextField(verbose_name='Blogning tavsifi')


    def __str__(self):
        return self.title

class Contact(models.Model):
    full_name = models.CharField(max_length=50,verbose_name="To'liq ism")
    email = models.EmailField(verbose_name='Email pochta')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$',
                                 message="Phone number must be entered in the format: '+998999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(verbose_name="Telefon raqam",validators=[phone_regex], max_length=13, blank=True)  # validators should be a list
    message = models.TextField(verbose_name="Xabar")

    def __str__(self):
        return self.full_name

class Review(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="To'liq ism")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$',
                                 message="Phone number must be entered in the format: '+998999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(verbose_name="Telefon raqam", validators=[phone_regex], max_length=13,
                                    blank=True)  # validators should be a list
    message = models.TextField(verbose_name="Xabar")

    def __str__(self):
        return self.full_name

class Review_for_business(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="To'liq ism")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$',
                                 message="Phone number must be entered in the format: '+998999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(verbose_name="Telefon raqam", validators=[phone_regex], max_length=13,
                                    blank=True)  # validators should be a list
    company = models.CharField(max_length=40,verbose_name="Kompaniya nomi")

    def __str__(self):
        return self.company

class Newsletter(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email