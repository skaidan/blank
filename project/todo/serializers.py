from rest_framework import serializers
from todo.models import Read 

class ReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Read
        fields = '__all__'
