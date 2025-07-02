from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from .serializers import RegisterSerializer

class RegisterView(CreateModelMixin, GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
