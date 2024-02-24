from django.urls import path
from .views import *

urlpatterns = [
    path('books/', book_list, name='books'),
    path('books/<int:id>', book_details, name='books')

]
