from rest_framework import serializers
from app.models import Category, EntryField

class EntryFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryField
        fields = ['id', 'category', 'open', 'close', 'open_sum', 'close_sum',]


class CategorySerializer(serializers.ModelSerializer):
    entryfield = EntryFieldSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'open_entry_time', 'close_entry_time', 'entryfield']

class CategoryPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'open_entry_time', 'close_entry_time']

class EntryFieldPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryField
        fields = ['id', 'category', 'open', 'close']