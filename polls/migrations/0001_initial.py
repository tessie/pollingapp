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

        # Adding model 'Choice1'
        db.create_table(u'polls_choice1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Poll'])),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'polls', ['Choice1'])

        # Adding model 'Choice2'
        db.create_table(u'polls_choice2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Poll'])),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'polls', ['Choice2'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'polls_poll')

        # Deleting model 'Choice1'
        db.delete_table(u'polls_choice1')

        # Deleting model 'Choice2'
        db.delete_table(u'polls_choice2')


    models = {
        u'polls.choice1': {
            'Meta': {'object_name': 'Choice1'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'polls.choice2': {
            'Meta': {'object_name': 'Choice2'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['polls']