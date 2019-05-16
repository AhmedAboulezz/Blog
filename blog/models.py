from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.CharField(max_length=140)
    tags = models.CharField(max_length=25)

    # def save(self, *args, **kwargs):
    #     if self.__class__.objects.filter(user=self.user).count() > 2:
    #         raise ValidationError("Too Much")
    #     return super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return "Blog #"+str(self.id)+" written by "+'"'+str(self.user)+'"'



