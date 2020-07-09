from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class Skill_level(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)
    instrument = models.CharField(max_length=50, blank=True, null=True)
    since = models.DateField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    skill = models.ManyToManyField(Skill_level,  blank=True)
    teacher = models.ForeignKey('self',on_delete=models.CASCADE,  related_name='teacher_name')

    REQUIRED_FIELDS = ['groups_id', 'email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
