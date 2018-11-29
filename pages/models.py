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


class StimSets(models.Model):
    stimsetid = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stimsetname = models.CharField(max_length=96)

    def __str__(self):
        return self.stimsetname

    def save(self, *args, **kwargs):
        super(StimSets, self).save(*args, **kwargs)


class Stims(models.Model):
    stimid = models.AutoField(primary_key=True)
    stimr = models.IntegerField(default=0)
    stimg = models.IntegerField(default=0)
    stimb = models.IntegerField(default=0)
    stimlabel = models.CharField(max_length=96)
    labelr = models.IntegerField(default=0)
    labelg = models.IntegerField(default=0)
    labelb = models.IntegerField(default=0)
    stimshape = models.CharField(max_length=25, blank=True, null=True)
    stimsetid = models.ForeignKey(StimSets, on_delete=models.CASCADE)

    def __str__(self):
        return self.stimlabel

    def save(self, *args, **kwargs):
        super(Stims, self).save(*args, **kwargs)
