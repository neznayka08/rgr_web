from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer, UserRegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Корневое API (возвращает наличие API и ссылку на видео)
@api_view(['GET'])
def api_root(request):
    return Response({
        'videos': request.build_absolute_uri('/api/videos/'),
        'register': request.build_absolute_uri('/api/auth/register/'),
        'login': request.build_absolute_uri('/api/auth/login/'),
    })

# Простая домашняя страница для проверки работы сервера
@api_view(['GET'])
def home(request):
    return Response({"message": "Добро пожаловать на видеоплатформу API!"})

# CRUD для видео
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        # Привязываем загружаемое видео к аутентифицированному пользователю
        serializer.save(user=self.request.user)

# Регистрация нового пользователя
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = UserRegisterSerializer.Meta.model.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": serializer.data,
                "message": "Пользователь успешно зарегистрирован."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)