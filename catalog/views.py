from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from .auth import require_api_key
from rest_framework.parsers import MultiPartParser, FormParser

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return super().get(request)

    @require_api_key
    def post(self, request):
        return super().post(request)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @require_api_key
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @require_api_key
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

from rest_framework.views import APIView
class UploadCoverView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    @require_api_key
    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return JsonResponse({"error": "BOOK_NOT_FOUND"}, status=404)

        file = request.FILES.get("cover")
        if not file:
            return JsonResponse({"error": "NO_FILE", "message": "No file uploaded."}, status=400)

        if file.size > 2 * 1024 * 1024:
            return JsonResponse({"error": "FILE_TOO_LARGE"}, status=413)

        allowed_types = ['image/jpeg', 'image/png', 'image/webp']
        if file.content_type not in allowed_types:
            return JsonResponse({
                "error": "INVALID_FILE_TYPE",
                "message": "Only JPG, PNG, and WEBP files are allowed",
                "allowed_types": ["jpg", "png", "webp"],
                "received_type": file.content_type.split('/')[-1]
            }, status=400)

        book.cover_image = file
        book.save()
        return JsonResponse({
            "id": book.id,
            "title": book.title,
            "cover_url": request.build_absolute_uri(book.cover_image.url),
            "message": "Cover uploaded successfully"
        }, status=200)
