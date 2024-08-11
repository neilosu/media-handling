from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.cloud import storage
from django.http import JsonResponse

class ImageUploadView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES['file']
        client = storage.Client()
        bucket = client.bucket('test-media-osu')
        blob = bucket.blob(image.name)

        blob.upload_from_file(image, content_type=image.content_type)
        file_url = f"https://storage.googleapis.com/{bucket.name}/{blob.name}"

        return JsonResponse({'file_url': file_url}, status=status.HTTP_201_CREATED)
