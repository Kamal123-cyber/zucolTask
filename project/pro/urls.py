from django.urls import path
from .views import SubjectAPIView, QuestionAPIView, AnswerAPIView

urlpatterns = [
    path('Subject/', SubjectAPIView.as_view()),
    path('Subject/<str:pk>', SubjectAPIView.as_view()),
    path('Question/', QuestionAPIView.as_view()),
    path('Question/<str:pk>', QuestionAPIView.as_view()),
    path('Answer/', AnswerAPIView.as_view()),
    path('Answer/<str:pk>', AnswerAPIView.as_view()),

]