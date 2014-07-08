# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'polls_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Poll'])),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'polls', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'polls_comment')


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
        u'polls.comment': {
            'Meta': {'object_name': 'Comment'},
            'Poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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