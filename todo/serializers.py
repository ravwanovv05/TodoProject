from rest_framework.serializers import ModelSerializer

from todo.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class UpdateDestroyTodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('text',)
