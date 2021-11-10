
from django.conf.urls import include
from django.urls import path
from .views import home, todoList, todoListCreate, toDo_list, todoListUpdate, todoListDelete, toDo_detail, TodoList, TodoDetail, TodoListCreate, TodoRetrieveUpdateDelete, TodoConcListCreate, TodoConcRetrieveUpdateDelete, TodoVSListRetreive, todoMVS

from rest_framework import routers

router = routers.DefaultRouter()
router.register('todoVs-list', TodoVSListRetreive)
router.register('todoMVS', todoMVS)

urlpatterns = [
    path('', home),
    path('todoList/', todoList), 
    path('todoListCreate/', todoListCreate),   
    path('toDo_list/', toDo_list), 
    path('todoListUpdate/<int:pk>/', todoListUpdate),  
    path('todoListDelete/<int:pk>/', todoListDelete),    
    path('toDo_detail/<int:pk>/', toDo_detail),  
    path('todo-list/',TodoList.as_view()),  
    path('todo-detail/<int:pk>/',TodoDetail.as_view()),  
    path('todo-create/',TodoListCreate.as_view()),  
    path('todo-retrieve/<int:pk>/',TodoRetrieveUpdateDelete.as_view()),  
    path('todo-concretrieve/<int:pk>/',TodoConcRetrieveUpdateDelete.as_view()),  
    path('todo-concrete/<int:pk>/',TodoConcListCreate.as_view()),  
    path('todo-concrete/',TodoConcListCreate.as_view()),  
    path('',include(router.urls)),  
    
]