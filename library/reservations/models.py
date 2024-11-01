from django.db import models
from django.contrib.auth import get_user_model

from reservations.managers import ReservationManager


class Author(models.Model):
    models
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('checked_out', 'Checked Out'),
    ]

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField()
    image_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="available")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def is_available(self):
        return self.status == "available"


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('reserved', 'Reserved'),
        ('checked_out', 'Checked Out'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled')
    ]

    objects = ReservationManager()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='reserved')

    def __str__(self):
        return f"Reservation of {self.book} by {self.user}"

    def cancel(self):
        if self.status != "reserved":
            return None
        self.book.status = "available"
        self.book.save()
        self.status = "cancelled"

        return self

    def checkout(self):
        if self.status not in ('reserved', 'available'):
            return None

        self.status = "checked_out"
        self.book.status = "checkout_out"
        return self
