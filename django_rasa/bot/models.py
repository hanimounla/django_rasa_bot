from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def save_file(string, path):
    if default_storage.exists(path):
        default_storage.delete(path)
    default_storage.save(path, ContentFile(string))
    

def create_bot_files():
    nlu_file_path = 'rasa_files/data/nlu.yml'
    domain_file_path = 'rasa_files/domain.yml'
    stories_file_path = 'rasa_files/data/stories.yml'
    
    nlu_string = "version: \"3.0\" \n \nnlu: \n"
    for category in QuestionCategory.objects.all():
        nlu_string += f"- intent: {category} \n     examples: \n"
        for question in Question.objects.filter(question_category=category):
            nlu_string += f"        - {question} \n"
        nlu_string += "\n \n"
    save_file(nlu_string, nlu_file_path)
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
                for answer in Answer.objects.filter(question=question):
                    domain_string += f"    - text: {answer} \n"
        domain_string += "\n \n"
    save_file(domain_string, domain_file_path)
    
    stories_string = "version: \"3.0\" \n \nstories: \n"
    
    for story in Story.objects.all():
        stories_string += f"- story: {story.title}\n steps: \n"
        for action in Action.objects.filter(story=story):
            stories_string += f"    - action: {action.title} \n"
        stories_string += "\n \n"
    save_file(stories_string, stories_file_path)
    
class QuestionCategory(models.Model):
    name = models.CharField("Question Category Name", max_length=50)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Question Category"
        verbose_name_plural = "Question Categories"


class Question(models.Model):
    question_text = models.CharField("Question Text", max_length=50)
    question_category = models.ManyToManyField(
        QuestionCategory, related_name="categories"
    )

    def __str__(self):
        return self.question_text
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answer(models.Model):
    answer_text = models.CharField("Answer Text", max_length=50)
    question = models.ManyToManyField(Question, related_name="questions")

    def __str__(self):
        return self.answer_text
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        
        
class Story(models.Model):
    title = models.CharField("Story Title", max_length=50)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"
        

class Action(models.Model):
    title = models.CharField("Action Title", max_length=50)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Action"
        verbose_name_plural = "Actions"
