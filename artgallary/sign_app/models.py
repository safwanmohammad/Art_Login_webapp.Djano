from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class Register(models.Model):
    user_name = models.CharField(max_length=100,null=False)
    password = models.TextField(null=False)
    email = models.EmailField(null=False)
    phone_no = models.IntegerField(null=False)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Register, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user_name
    


