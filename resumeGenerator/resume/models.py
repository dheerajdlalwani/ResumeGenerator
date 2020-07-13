from django.db import models
from datetime import date
from django.contrib.auth.models import User
import datetime
# Create your models here.


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150, blank = True)
    email = models.CharField(max_length=254)
    date_of_birth = models.DateField()
    current_position = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=254)
    github = models.CharField(max_length=254)
    twitter = models.CharField(max_length=254)
    contact = models.CharField(max_length=254)
    intro = models.TextField()
    skill_1 = models.CharField(max_length=25)
    skill_2 = models.CharField(max_length=25)
    skill_3 = models.CharField(max_length=25)
    skill_4 = models.CharField(max_length=25)
    skill_5 = models.CharField(max_length=25)
    skill_6 = models.CharField(max_length=25)
    skill_7 = models.CharField(max_length=25)
    project_1_name = models.CharField(max_length=25)
    project_1_description = models.TextField()
    project_1_github = models.CharField(max_length=254)
    project_2_name = models.CharField(max_length=25)
    project_2_description = models.TextField()
    project_2_github = models.CharField(max_length=254)
    project_3_name = models.CharField(max_length=25)
    project_3_description = models.TextField()
    project_3_github = models.CharField(max_length=254)
    project_4_name = models.CharField(max_length=25)
    project_4_description = models.TextField()
    project_4_github = models.CharField(max_length=254)
    internship_1_title = models.CharField(max_length=200)
    internship_1_description = models.TextField()
    internship_2_title = models.CharField(max_length=200)
    internship_2_description = models.TextField()
    internship_3_title = models.CharField(max_length=200)
    internship_3_description = models.TextField()
    education_1_title = models.CharField(max_length=100)
    education_1_description = models.TextField()
    education_2_title = models.CharField(max_length=100)
    education_2_description = models.TextField()
    language_1 = models.CharField(max_length=50)
    language_2 = models.CharField(max_length=50)
    language_3 = models.CharField(max_length=50)
    language_4 = models.CharField(max_length=50)
    language_5 = models.CharField(max_length=50)
    certification_1 = models.CharField(max_length=200)
    certification_2 = models.CharField(max_length=200)
    certification_3 = models.CharField(max_length=200)
    certification_4 = models.CharField(max_length=200)





    

