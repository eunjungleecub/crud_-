from django.urls import path

from . import views

urlpatterns = [
    path('', , name='home')
    path('all/', views.BookList.as_view(), name='all_books'),
    path('new/', BookCreate.as_view(), name='create'),
    path('show/<int:pk>', BookView.as_view(), name='show'),
    path('edit/<int:pk>', BookUpdate.as_view(), name='edit'),