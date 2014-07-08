# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'polls_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'polls', ['Poll'])

        # Adding model 'Choice'
        db.create_table(u'polls_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Poll'])),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=45)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'polls', ['Choice'])

        # Adding model 'Comment'
        db.create_table(u'polls_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Poll'])),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('latest', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'polls', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'polls_poll')

        # Deleting model 'Choice'
        db.delete_table(u'polls_choice')

        # Deleting model 'Comment'
        db.delete_table(u'polls_comment')


    models = {
        u'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '45'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'polls.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.BooleanField', [], {}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['polls']