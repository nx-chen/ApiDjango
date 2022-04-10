from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from Api.models import Book
from Api.serializers import ApiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def book_list(request):
    """
    description: User description
    get:
    Return all books in the database
    post:
    Create a new book
    delete:
    Delete all books in the database
    """
    if request.method == 'GET':
        books = Book.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            books = books.filter(title__icontains=title)

        tutorials_serializer = ApiSerializer(books, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'POST':
        api_data = JSONParser().parse(request)
        api_serializer = ApiSerializer(data=api_data)
        if api_serializer.is_valid():
            api_serializer.save()
            return JsonResponse(api_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Book.objects.all().delete()
        return JsonResponse(
            {'message': '{} books were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    """
        get:
        Return the book which id is {id} in the database
        put:
        Modify the book which id is {id} in the database
        delete:
        Delete the book which id is {id} in the database
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        api_serializer = ApiSerializer(book)
        return JsonResponse(api_serializer.data)

    elif request.method == 'PUT':
        api_data = JSONParser().parse(request)
        api_serializer = ApiSerializer(book, data=api_data)
        if api_serializer.is_valid():
            api_serializer.save()
            return JsonResponse(api_serializer.data)
        return JsonResponse(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

