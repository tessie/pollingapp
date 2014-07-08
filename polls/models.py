from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=300)
    pub_date = models.DateField()

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    text = models.TextField(max_length=45)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text




class Comment(models.Model):
    poll = models.ForeignKey(Poll)
    comment = models.TextField(max_length=300)
    post_date = models.DateTimeField()
    latest = models.BooleanField()


    def __unicode__(self):
        return self.comment
