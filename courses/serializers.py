from rest_framework import serializers

from courses.models import SubLesson, Lesson, Course, Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('pk', 'question', 'answer',)


class SubLessonSerializer(serializers.ModelSerializer):
    # lesson = LessonSerializer()
    quizes = serializers.SerializerMethodField()

    def get_quizes(self, obj: Quiz):
        return QuizSerializer(obj.quiz.all(), many=True).data

    class Meta:
        model = SubLesson
        fields = ('pk', 'title', 'content', 'image', 'quizes',)


class LessonSerializer(serializers.ModelSerializer):
    # course = CourseSerializer()
    sublessons = serializers.SerializerMethodField()

    def get_sublessons(self, obj: SubLesson):
        return SubLessonSerializer(obj.sublessons.all(), many=True).data

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'overview', 'summary', 'prerequisites', 'sublessons',)


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    def get_lessons(self, obj: Lesson):
        return LessonSerializer(obj.lessons.all(), many=True).data

    class Meta:
        model = Course
        fields = ('pk', 'title', 'description', 'level', 'duration', 'lessons',)
