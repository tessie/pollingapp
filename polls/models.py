from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField(max_length=300)
    pub_date = models.DateField()

    def __unicode__(self):
        return self.question


class Choice1(models.Model):
    poll     =models.ForeignKey(Poll)
    text  =   "Yes you are the only one"
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text


class Choice2(models.Model):
    poll    =models.ForeignKey(Poll)
    text = "No you are not the only one"
    votes= models.IntegerField(default=0)

    def __unicode__(self):
        return self.text


class Comment(models.Model):
    Poll   =models.ForeignKey(Poll)
    comment =models.TextField(max_length=300)
    post_date = models.DateTimeField()

    def __unicode__(self):
        return self.comment

