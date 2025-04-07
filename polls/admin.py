from django.contrib import admin
from .models import Question, Choice

"""
 Registering the Question and Choice models
 """
admin.site.register(Question)
admin.site.register(Choice)