from rest_framework.serializers import ModelSerializer

from clock.models import Clock


class ClockSerializer(ModelSerializer):
    class Meta:
        model = Clock
        fields = '__all__'
