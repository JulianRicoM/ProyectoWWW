from django.urls import path
from .views import UsersList, UserDetail

urlpatterns = [
    path('', UsersList.as_view()),
    path('<int:id>', UserDetail)
]