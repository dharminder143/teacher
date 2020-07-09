from django.shortcuts import render
from rest_framework import status,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from user.permission import IsAdminUser, IsLoggedInUserOrAdmin, IsAdminOrStudentUser
from user.models import User
from user.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from django.db.models import Q


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['groups']
    search_fields = ['username','first_name','last_name','email']

    def get_queryset(self):
        teacher = User.objects.filter(teacher=self.request.user,groups="2")
        admin= User.objects.filter(teacher=self.request.user,groups="3")

        if teacher.exists():
            queryset = User.objects.filter(teacher=self.request.user)
        elif admin.exists():
            queryset = User.objects.filter()
        else:
            queryset = User.objects.filter(Q(groups="2")| Q(groups="3"))
        return queryset

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminOrStudentUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]

    @action(
        methods=["get"],
        detail=False,
        url_path="assistant",
        url_name="assistant",
        permission_classes=[IsAuthenticated],
        serializer_class=UserSerializer,
    )
    def assistant(self, request):
        serializer_class = UserSerializer
        queryset = User.objects.filter()
        serializer = self.serializer_class(queryset,many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
