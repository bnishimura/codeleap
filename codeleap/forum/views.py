from django.shortcuts import render

from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def root(request):
    # get items
    if request.method == "GET":
        app = Item.objects.all()
        serializer = ItemSerializer(app, many=True)
        return Response(serializer.data)

    # post item
    elif request.method == "POST":
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# expect /careers/{id}
@api_view(['DELETE', 'PATCH'])
def itemMutate(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response({'error': "Item not found"}, status=404)

    # delete item
    if request.method == 'DELETE':
        item.delete()
        return Response({'message': "Item deleted successfully"}, status=204)

    # update item
    elif request.method == 'PATCH':
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save()
        return Response(serializer.data, status=200)
