"""learning_logs/admin.py"""

# Django modules
from django.contrib import admin

# My modules
from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)