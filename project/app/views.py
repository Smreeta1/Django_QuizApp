from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import QuestionSerializer, ScoreBoardSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serialized_courses = [{'id': course.id, 'course_name': course.course_name} for course in courses]
    return Response(serialized_courses)

@api_view(['GET'])
def api_question(request, id):
    raw_questions = Question.objects.filter(course=id)[:20]
    serializer = QuestionSerializer(raw_questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def check_score(request):
    user = request.user
    data = request.data
    course_id = data.get('course_id')
    solutions = data.get('data')
    course = Course.objects.get(id=course_id)
    score = 0
    for solution in solutions:
        question = Question.objects.filter(id=solution.get('question_id')).first()
        if question.answer == solution.get('option'):
            score += question.marks
    score_board_data = {'course': course_id, 'score': score, 'user': user.id}
    serializer = ScoreBoardSerializer(data=score_board_data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'success', 'status': True}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
