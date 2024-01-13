from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    CHOICE = [
        ('smartphone', 'Смартфоны'),
        ('food', 'Еда'),
        ('cars', 'Машины'),
    ]
    name = models.CharField(max_length=50, blank=False, null=False)
    category = models.CharField(max_length=50, blank=False, null=False, choices=CHOICE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    text = models.TextField(blank=False, null=False)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.product} - {self.rating}"

    def average_rating(self):
        moderated_reviews = self.review_set.filter(moderated=True)
        if moderated_reviews.exists():
            return moderated_reviews.aggregate(models.Avg('rating'))['rating__avg']
        return 0