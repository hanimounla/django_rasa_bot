from django.contrib import admin

from .models import QuestionCategory, Question, Answer, Story, Action, Intent

    
admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Story)
admin.site.register(Action)
admin.site.register(Intent)
