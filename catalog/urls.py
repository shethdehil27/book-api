from django.urls import path
from .views import BookList, BookDetail, UploadCoverView

urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),
    path('books/<int:pk>/upload-cover/', UploadCoverView.as_view()),
]
