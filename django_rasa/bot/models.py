from pyexpat import model
from django.db import models


class QuestionCategory(models.Model):
    name = models.CharField("Question Category Name", max_length=50)

    def __str__(self):
        return self.name

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

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answer(models.Model):
    answer_text = models.CharField("Answer Text", max_length=50)
    question = models.ManyToManyField(Question, related_name="questions")

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
