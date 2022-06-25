
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import  *

class QoshiqchiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qoshiqchi
        fields = "__all__"


class AlbomSerializer(serializers.ModelSerializer):
    qoshiqchi = QoshiqchiSerializer()
    class Meta:
        model = Albom
        fields = "__all__"


class QoshiqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qoshiq
        fields = "__all__"
    def validate_file(self, qiymat, ):
        if qiymat.enswith(".mp3")==False:
            raise ValidationError("Bunday url yo'q")
        return qiymat
