from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import SerializedBook
from .models import BookList
# Create your views here.

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        book_data = BookList.objects.all()
        serializer = SerializedBook(book_data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        add_book = SerializedBook(data=request.data)
        if add_book.is_valid():
            add_book.save()
            return Response(add_book.data, status=status.HTTP_201_CREATED)

 
@api_view(['GET', 'PUT', 'DELETE'])
def book_details(request, id):

    book_data = get_object_or_404(BookList, id=id)
    
    if request.method == 'PUT':
        serialized_data = SerializedBook(book_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book_data.delete()
        return Response(status=status.HTTP_200_OK)
    
    serialized_data = SerializedBook(book_data)
    return Response(serialized_data.data)