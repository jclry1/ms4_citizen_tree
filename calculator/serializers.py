from rest_framework import serializers
from .models import faq

class faqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=faq
        fields = ('id', 'question_name', 'question_answer')