from django.urls import path, include
from app.views import CategoryView, EntryFieldView, EntryFieldPut, CategoryPut, EntryFieldPost, CategoryPost



urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('categorypost/', CategoryPost.as_view()),
    path('categoryput/<int:pk>/', CategoryPut.as_view()),
    path('entryfield/', EntryFieldView.as_view()),
    path('entryfieldpost/', EntryFieldPost.as_view()),
    path('entryfieldput/<int:pk>/', EntryFieldPut.as_view()),
]
