from rest_framework import serializers 
from videos.models import History, Bookmark
 
 
class HistorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = History
        fields = ('id',
                  'video_link',
                  'date_field')

class BookmarkSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Bookmark
        fields = ('id',
                  'bookmark_link')