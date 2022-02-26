from django.contrib import admin
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .models import QuestionCategory, Question, Answer


def create_bot_files():
    nlu_file_path = 'rasa_files/data/nlu.yml'
    domain_file_path = 'rasa_files/domain.yml'
    
    nlu_string = "version: \"3.0\" \n \nnlu: \n"
    for category in QuestionCategory.objects.all():
        nlu_string += f"- intent: {category} \n     examples: \n"
        for question in Question.objects.filter(question_category=category):
            nlu_string += f"        - {question} \n"
        nlu_string += "\n \n"
        
    if default_storage.exists(nlu_file_path):
        default_storage.delete(nlu_file_path)
    default_storage.save(nlu_file_path, ContentFile(nlu_string))
    
    domain_string = "version: \"3.0\" \n \nintents: \n"
    for category in QuestionCategory.objects.all():
        domain_string += f" - {category} \n"
        
    domain_string += "\n \nresponses: \n"
    
    for category in QuestionCategory.objects.all():
        domain_string += f"     utter_{category}: \n"
        for question in Question.objects.filter(question_category=category):
            try:
                domain_string += f"    - text: {Answer.objects.get(question=question)} \n"
            except:
                pass
        domain_string += "\n \n"
            
    if default_storage.exists(domain_file_path):
        default_storage.delete(domain_file_path)
    default_storage.save(domain_file_path, ContentFile(domain_string))
         
        
class BotAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        create_bot_files()
        super().save_model(request, obj, form, change)
    
admin.site.register(QuestionCategory, BotAdmin)
admin.site.register(Question, BotAdmin)
admin.site.register(Answer, BotAdmin)
