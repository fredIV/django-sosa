from django.db import models
from users.models import CustomUser
from django.forms import ModelForm

# Create your models here.


class Boards(models.Model):
    boardid = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    boardname = models.CharField(max_length=96)
    boardr = models.IntegerField(default=0)
    boardg = models.IntegerField(default=0)
    boardb = models.IntegerField(default=0)
    boardtiltx = models.IntegerField(default=0)
    boardtilty = models.IntegerField(default=0)
    boardbackgroundr = models.IntegerField(default=0)
    boardbackgroundg = models.IntegerField(default=0)
    boardbackgroundb = models.IntegerField(default=0)

    def __str__(self):
        return self.boardname

    def save(self, *args, **kwargs):
        super(Boards, self).save(*args, **kwargs)


TITLE_CHOICES = (
    ('Cone.', 'CONE'),
    ('Cylinder.', 'CYLINDER'),
    ('Cube.', 'CUBE'),
)


class Stims(models.Model):
    stemsetid = models.AutoField(primary_key=True)
    stimr = models.IntegerField(default=0)
    stimg = models.IntegerField(default=0)
    stimb = models.IntegerField(default=0)
    stimlabel = models.CharField(max_length=96)
    labelr = models.IntegerField(default=0)
    labelg = models.IntegerField(default=0)
    labelb = models.IntegerField(default=0)
    stimshape = models.CharField(max_length=25, blank=True, null=True, choices=TITLE_CHOICES)

    def __str__(self):
        return self.stimlabel

    def save(self, *args, **kwargs):
        super(Boards, self).save(*args, **kwargs)