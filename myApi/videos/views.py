from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from videos.models import History, Bookmark
from videos.serializers import BookmarkSerializer, HistorySerializer
from rest_framework.decorators import api_view
from django.db.models import Max


@api_view(['GET', 'POST', 'DELETE'])
def history_list(request):
    if request.method == 'GET':
        historys = History.objects.all().order_by('-id')
        
        history_serializer = HistorySerializer(historys, many=True)
        return JsonResponse(history_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        history_data = JSONParser().parse(request)
        history_serializer = HistorySerializer(data=history_data)
        if history_serializer.is_valid():
            history_serializer.save()
            return JsonResponse(history_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = History.objects.all().delete()
        return JsonResponse({'message': '{} Videos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def history_detail(request, pk):
    try: 
        history = History.objects.get(pk=pk) 
    except History.DoesNotExist: 
        return JsonResponse({'message': 'The video does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        history_serializer = HistorySerializer(history) 
        return JsonResponse(history_serializer.data) 
 
    elif request.method == 'PUT': 
        history_data = JSONParser().parse(request) 
        history_serializer = HistorySerializer(history, data=history_data) 
        if history_serializer.is_valid(): 
            history_serializer.save() 
            return JsonResponse(history_serializer.data) 
        return JsonResponse(history_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        history.delete() 
        return JsonResponse({'message': 'Video was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST', 'DELETE'])
def bookmark_list(request):
    if request.method == 'GET':
        bookmarks = Bookmark.objects.all().order_by('-id')
        
        bookmark_serializer = BookmarkSerializer(bookmarks, many=True)
        return JsonResponse(bookmark_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        bookmark_data = JSONParser().parse(request)
        bookmark_serializer = BookmarkSerializer(data=bookmark_data)
        if bookmark_serializer.is_valid():
            bookmark_serializer.save()
            return JsonResponse(bookmark_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(bookmark_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bookmark.objects.all().delete()
        return JsonResponse({'message': '{} Videos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)        


@api_view(['GET', 'PUT', 'DELETE'])
def bookmark_detail(request, pk):
    try: 
        bookmark = Bookmark.objects.get(pk=pk) 
    except Bookmark.DoesNotExist: 
        return JsonResponse({'message': 'The video does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bookmark_serializer = BookmarkSerializer(bookmark) 
        return JsonResponse(bookmark_serializer.data) 
 
    elif request.method == 'PUT': 
        bookmark_data = JSONParser().parse(request) 
        bookmark_serializer = BookmarkSerializer(bookmark, data=bookmark_data) 
        if bookmark_serializer.is_valid(): 
            bookmark_serializer.save() 
            return JsonResponse(bookmark_serializer.data) 
        return JsonResponse(bookmark_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        bookmark.delete() 
        return JsonResponse({'message': 'Video was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def bookmark_total(request):
    if request.method == 'GET':
        bookmarkscount = Bookmark.objects.all().count()
        return JsonResponse(bookmarkscount, safe=False)
        # 'safe=False' for objects serialization