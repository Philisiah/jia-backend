"""jia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from courses.views import LessonCatalog, LessonRetrieve,SubLessonCatalog, SubLessonRetrieve, CourseCatalog, CourseRetrieve, QuizCatalog, QuizRetrieve

app_name = 'courses'

urlpatterns = [
    path('lessons/', LessonCatalog.as_view(), name="allessons"),
    path('lesson/details/<int:pk>/', LessonRetrieve.as_view(), name="lesson-details"),
    path('sublessons/', SubLessonCatalog.as_view(), name="asublessons"),
    path('sublesson/details/<int:pk>/', SubLessonRetrieve.as_view(), name="sublesson-details"),
    path('courses/', CourseCatalog.as_view(), name="courses"),
    path('course/details/<int:pk>/', CourseRetrieve.as_view(), name="'course-details"),
    path('quizes/', QuizCatalog.as_view(), name="quizes"),
    path('quiz/details/<int:pk>/', QuizRetrieve.as_view(), name="quiz-details"),
]
