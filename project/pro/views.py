from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Subject, Question, Answer
from .serializers import SubjectSerializer, QuestionSerializer
from rest_framework.response import Response

class SubjectAPIView(APIView):

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SubjectSerializer(data)

        else:
            data = Subject.objects.all()
            serializer = SubjectSerializer(data, many=True)

            return Response(serializer.data)


class QuestionAPIView(APIView):

    def get_object(self, pk):
        try:
            return QuestionAPIView.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = QuestionSerializer(data)

        else:
            data = Question.objects.all()
            serializer = QuestionSerializer(data, many=True)

            return Response(serializer.data)
class AnswerAPIView(APIView):

    def get_object(self, pk):
        try:
            return AnswerAPIView.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = AnswerSerializer(data)

        else:
            data = Answer.objects.all()
            serializer = AnswerSerializer(data, many=True)

            return Response(serializer.data)

def post(self, request, format=None):
    data = request.data
    serializer = SubjectSerializer(data=data)

       
    serializer.is_valid(raise_exception=True)

    serializer.save()

    response = Response()

    response.data = {
        'question': 'what is newton 3rd law of motion',
        'data': serializer.data
    }

    return response

def put(self, request, pk=None, format=None):  
    question_to_update = Question.objects.get(pk=pk)
    serializer = QuestionSerializer(instance=question_to_update,data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = Response()
    response.data = {
        'question': 'what is the newton 2nd law',
        'data': serializer.data
    }

    return response

def delete(self, request, pk, format=None):
        question_to_delete =  Question.objects.get(pk=pk)

        question_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })
