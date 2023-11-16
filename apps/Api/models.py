from django.db import models

# Create your models here.

class CinemaStudio(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    logo = models.ImageField(upload_to='cs', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

# MOVIE AGE ALLOWED
CLASIFICATION = [
    ('-18', '-18'),
    ('+18', '+18')
]

class Movie(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='movies', null=True, blank=False)
    resume = models.TextField()
    clasification = models.CharField(max_length=5, choices=CLASIFICATION)
    release_date = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender')
    created_by = models.ForeignKey(CinemaStudio, on_delete=models.CASCADE, related_name='studio')
    available = models.BooleanField(default=True) 
    # LOGIC ELIMINATION
    state = models.BooleanField(default=True) 

    def __str__(self) -> str:
        return f"{self.name} - {self.gender}"
