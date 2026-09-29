from rest_framework  import serializers
from .models import PredictAlive

class PredictAliveSerializer(serializers.ModelSerializer):
    class Meta:
        model=PredictAlive
        fields=['Pclass','Sex','Age','Fare','Family','Embarked','predict_alive']