
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import  *

class QoshiqchiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qoshiqchi
        fields = "__all__"


class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = "__all__"
    def validate_nom(self, qiymat, ):
        if len(qiymat)<4:
            raise ValidationError("Bunday albom yo'q")
        return qiymat
class QoshiqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qoshiq
        fields = "__all__"
    def validate_janr(self, qiymat, ):
        A = ["Mumtoz", "Rep", "Pop", "Jazz"]
        for i in A:
            if (qiymat!=i):
                raise ValidationError("Bunday janr yo'q")
            return qiymat
