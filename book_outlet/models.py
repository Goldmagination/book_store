from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def fullCountry(self):
        return f"{self.name}, {self.code}"
    def __str__(self):
        return self.fullCountry()

    class Meta:
        verbose_name_plural="Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postcode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def fullAddress(self):
        return f"{self.street}, {self.postcode}, {self.city}"
    def __str__(self):
        return self.fullAddress()

    class Meta:
        verbose_name_plural="Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="author", null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=75)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    price = models.IntegerField()
    slug = models.SlugField(default="", null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, related_name="books")

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug= slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title},(rating: {self.rating}),and price:{self.price}"
