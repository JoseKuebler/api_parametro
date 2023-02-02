from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import *

class ParamaetroListApiView(APIView):

    def get(self, request, *args, **kwargs):

        todos =  ParametroModel.objects.filter(user = request.user.id)
        if todos.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = ParametroModelSerializer(todos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):

        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed')
        }
        serializer = ParametroModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        todos = ParametroModel.objects.all()
        todos.delete()
        return Response(status=status.HTTP_200_OK)