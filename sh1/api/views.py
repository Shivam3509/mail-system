from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,GenericAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin


class ListAPIView(RetrieveModelMixin,ListModelMixin,CreateModelMixin,GenericAPIView):
    serializer_class = StudentSerializer

    def get(self,request,*args, **kwargs):
        view =self.retrieve(request, *args, **kwargs) if request.query_params.get('pk',None) else self.list(request, *args, **kwargs)
        return view

    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get_queryset(self):
        id_ = self.kwargs.get('pk',None)
        if id_:
            queryset = Student.objects.filter(pk=id_)
        else:
            queryset = Student.objects.all()
        return queryset
    