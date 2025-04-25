from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, register_view, login_view, logout_view

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
        path('register/', register_view),
        path('login/', login_view),
        path('logout/', logout_view),
        path('', include(router.urls)),
]
