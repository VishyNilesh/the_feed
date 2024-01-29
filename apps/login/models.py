from django.db import models
import re 
# Create your models here.


class UserManager(models.Manager):
    def validator(self, postData, pageType):
        errors = {}

        if pageType == 'registration' : #Register page checking
            pattern = re.compile("^[A-Za-z]+$")

        if len(postData['register_fname']) < 1:
            errors['register_fname'] = "First name is required"

        if len(postData['register_lname']) < 1:
            errors['register_lname'] = "Last name is required"

        pattern = re.compile("^[^\s@]+@[^\s@]+\.[^\s@]+$")

        if len(postData['register_email']) < 1:
            errors['register_email'] = "Email is required"

        elif not pattern.match(postData['register_email']):
            errors['register_email'] = "Please enter a valid email address !"

        checkEmail = User.objects.filter(email=postData['register_email']) #user model to verify from db

        if checkEmail:
            errors['register_email'] = "A user with email is already present in our db"

        if len(postData['register_pwd'])<1:
            errors['register_pwd'] = "Password is must"

        elif len(postData['register_pwd'])<8:
            errors['register_pwd'] = "Password must be atleast 8 characters"

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

