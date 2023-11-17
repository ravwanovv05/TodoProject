from django.urls import path
from todo.views import AddTodoAPIView, UpdateDestroyTodoGenericAPIView, OwnerTodoGenericAPIView, TodoInfoAPIView

urlpatterns = [
    path('add-todo', AddTodoAPIView.as_view(), name='add-todo'),
    path('update-delete/<int:pk>', UpdateDestroyTodoGenericAPIView.as_view(), name='update-delete'),
    path('owner-todo', OwnerTodoGenericAPIView.as_view(),  name='owner-todo'),
    path('todo-info/<int:pk>', TodoInfoAPIView.as_view(), name='todo-info'),
]

