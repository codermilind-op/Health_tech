# from django.db import models
#
#
#
# # Create your models here.
# from django.db import models
#
# class Condition(models.Model):
#     name = models.CharField(max_length=100)
#     symptoms = models.TextField(help_text="Comma-separated list of symptoms")  # comma-separated list of symptoms
#
#     def __str__(self):
#         return self.name


# symptom_checker/models.py
from django.db import models
from django.contrib.auth.models import User

class Condition(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.TextField(help_text="Comma-separated list of symptoms")
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Estimated cost of treatment")
    prescription = models.TextField(blank=True, null=True, help_text="Recommended prescription or treatment")

    def __str__(self):
        return self.name

class HealthcareFacility(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='facilities')

    def __str__(self):
        return self.name

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_terms = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
