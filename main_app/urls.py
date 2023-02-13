from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('accounts/signup/', views.signup, name='signup'),

    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]