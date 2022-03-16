from dataclasses import fields
from rest_framework import serializers

from webapp.models import DzongkhaWord

class dzongkhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DzongkhaWord
 #       fields = ('firstname', 'lastname', 'emp_id')
        fields = '__all__'