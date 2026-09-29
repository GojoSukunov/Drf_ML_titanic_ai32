from django.db import models

SEX_TYPE=(
('Male','Male'),
('Female','Female')
)
class PredictAlive(models.Model):
    Pclass=models.PositiveSmallIntegerField(default=0)
    Sex=models.CharField(max_length=6)
    Age=models.FloatField(default=0)
    Fare=models.FloatField(default=0)
    Family=models.PositiveSmallIntegerField(default=0)
    Embarked=models.CharField(max_length=32)
    predict_alive=models.PositiveSmallIntegerField(default=0)
