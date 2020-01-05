from django.db import models


# Create your models here.
class Course(models.Model):
    # a tour of qwiklabs for reference
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('intermediate', 'Advanced'),
    )
    title = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    level = models.CharField(default='beginner', choices=LEVEL_CHOICES, max_length=140)
    duration = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def lessons(self):
        return self.lessons.all()

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    # subtitles in tour of qwiklabs
    title = models.CharField(max_length=140, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    prerequisites = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='lessons')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def sub_lessons(self):
        return self.sublessons.all()

    def __str__(self):
        return f'{self.title}'


class SubLesson(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='sublessons')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def quiz(self):
        return self.quiz.all()

    def __str__(self):
        return f'{self.title}'


class Quiz(models.Model):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    sub_lesson = models.ForeignKey(SubLesson, on_delete=models.CASCADE, null=True, blank=True, related_name='quiz')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sub_lesson.title} + {self.question}'
