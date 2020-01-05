# Create your views here.
from rest_framework import generics

from courses.models import SubLesson, Course, Quiz, Lesson
from courses.serializers import SubLessonSerializer, CourseSerializer, QuizSerializer, LessonSerializer


# list views


class CourseCatalog(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class QuizCatalog(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class LessonCatalog(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class SubLessonCatalog(generics.ListCreateAPIView):
    queryset = SubLesson.objects.all()
    serializer_class = SubLessonSerializer


# get individual objects


class CourseRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class QuizRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class LessonRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class SubLessonRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubLesson.objects.all()
    serializer_class = SubLessonSerializer
