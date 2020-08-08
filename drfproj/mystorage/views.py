from rest_framework import viewsets
from .models import Essay, Album, Files #models.py의 Essay 모델
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset=Essay.objects.all()
    serializer_class= EssaySerializer

    filter_backends = [SearchFilter]
    search_fields =('title','body') #튜플로 작성 


    def perform_create(self, serializer): #직접 작성한 유저를 자동저장한다. self.user를 받아와야한다
        serializer.save(author=self.request.user)
    
    #현재 request를 보낸 유저는 self.request.user

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else: 
            qs = qs.none()
        return qs

class ImageViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class= AlbumSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset=Files.objects.all()
    serializer_class= FilesSerializer

