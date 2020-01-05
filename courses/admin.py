from django.contrib import admin

from courses.models import Quiz, SubLesson, Lesson, Course


# Register your models here.
# inlines
class LessonInlineAdmin(admin.TabularInline):
    model = Lesson


class SubLessonInlineAdmin(admin.TabularInline):
    model = SubLesson


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [SubLessonInlineAdmin]

@admin.register(SubLesson)
class SubLessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin]