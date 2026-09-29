from rest_framework.response import Response
from . import serializers
from .serializers import PredictAliveSerializer
from rest_framework import views
from pathlib import Path
import joblib
from rest_framework import status


base_dir=Path(__file__).resolve().parent.parent
path_model=base_dir/'model'/'model_titanic_ai32.pkl'
model=joblib.load(path_model)

class PredictAliveViewSet(views.APIView):
    def post(self,request):
        instance=serializers.PredictAliveSerializer(data=self.request.data)
        if instance.is_valid():
            data=instance.validated_data

            new_sex=data.pop('Sex')
            sex_0_1=[1 if new_sex=='female' else 0]
            new_embarked=data.pop('Embarked')
            embarked_0_1=[1 if new_embarked=='Q' else 0,
                          1 if new_embarked=='S' else 0]
            features=[
                data['Pclass'],
                data['Age'],
                data['Fare'],
                data['Family'],
            ]+sex_0_1+embarked_0_1
            prediction=int(model.predict([features])[0])
            pred_alive=instance.save(predict_alive=prediction)
            return Response({'prediction_survive':prediction,'data':PredictAliveSerializer(pred_alive).data},status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
