
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#importación de modelos
from loadImage.models import LoadImageModel

class LoadImageSerializer(serializers.ModelSerializer):
    
    def create(self, file):
        image = LoadImageModel.objects.create(
            name_img=file,
            url_img = 'http://localhost:8000/assets/img/'+str(file),
            format_img = str(file).split('.')[1]
        )
        return image
    class Meta:
        model =LoadImageModel
        fields = ('name_img',)


class LoadImageSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = LoadImageModel
        fields = ('__all__')
