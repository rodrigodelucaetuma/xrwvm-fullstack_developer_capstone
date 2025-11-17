# Uncomment the following imports before adding the Model code


from django.db import models
#from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model): 
    # - Many-To-One relationship to Car Make model (One Car Make has many
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(default=1,
    validators=[
        MaxValueValidator(50),
        MinValueValidator(1)
    ])

    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('PICKUP', 'Pickup'),
        ('VAN', 'Van'),
        ('Sport', 'Sport'),
        ('MICRO', 'Micro'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    year = models.IntegerField(default=2025,
    validators=[
        MaxValueValidator(2025),
        MinValueValidator(2015)
    ])
# - Any other fields you would like to include in car model

    def __str__(self):
        return self.name  # Return the name as the string representation
