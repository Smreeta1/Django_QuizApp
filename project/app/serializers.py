from rest_framework import serializers
from .models import Course, Question, ScoreBoard


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ScoreBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreBoard
        fields = '__all__'
