from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer, UpdateDestroyTodoSerializer

User = get_user_model()


# generic
class AddTodoAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def post(self, request):
        todo_serializer = self.get_serializer(data=request.data)
        todo_serializer.is_valid(raise_exception=True)
        todo_serializer.save()
        return Response(todo_serializer.data)


# for user
class UpdateDestroyTodoGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateDestroyTodoSerializer

    def get_object(self, pk):
        return Todo.objects.get(pk=pk)

    def patch(self, request, pk):
        todo = self.get_object(pk)

        serializer_todo = self.get_serializer(todo, request.data, partial=True)
        serializer_todo.is_valid(raise_exception=True)
        serializer_todo.save()
        return Response(serializer_todo.data)

    def delete(self, request, pk):
        todo = self.get_object(pk)

        try:
            todo.delete()
        except Exception as e:
            return Response({'success': False, 'message': str(e)})
        return Response(status=204)


class OwnerTodoGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get(self,  request):
        todo = Todo.objects.filter(owner=request.user.id)
        serializer_todo = self.get_serializer(todo, many=True)
        return Response(serializer_todo.data)


class TodoInfoGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get(self, request, pk):
        owner = request.user.id
        todo = Todo.objects.get(Q(owner=owner) & Q(id=pk))
        todo_serializer = self.get_serializer(todo)
        return Response(todo_serializer.data)


