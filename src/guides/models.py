from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "User"  # Define table name 'User'

    def __str__(self):
        return self.name


class Guide(models.Model):
    trackingNumber = models.CharField(max_length=15, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    currentStatus = models.CharField(max_length=20)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Guide"  # Define table name 'Guide'

    def __str__(self):
        return f"Guía {self.trackingNumber} - {self.currentStatus}"


class Status(models.Model):
    # Using ForeignKey to connect directly with Guide Model
    guideId = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        db_column="guideId",
    )
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=20)

    class Meta:
        db_table = "StatusHistory"  # Define table name 'StatusHistory'

    def __str__(self):
        return f"Status {self.status} para Guía {self.guideId.trackingNumber}"
