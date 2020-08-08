from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')

class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True) #이미지가 잘 올라갔는지를 확인하는 작업을 url을 통해 확인하겠다는 코드 

    class Meta:
        model = Album
        fields =('pk','author_name','image','desc')

class FilesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True) #이미지가 잘 올라갔는지를 확인하는 작업을 url을 통해 확인하겠다는 코드 

    class Meta:
        model = Files
        fields =('pk','author','myfile','desc')