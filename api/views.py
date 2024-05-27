from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            username = serializer.validated_data.get('username')
            content = serializer.validated_data.get('content')
            if title and username and content:
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({"error": "Os campos title, username e content não podem ser vazios."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            username = serializer.validated_data.get('username')
            content = serializer.validated_data.get('content')
            if title and username and content:
                self.perform_update(serializer)
                return Response(serializer.data)
            else:
                return Response({"error": "Os campos title, username e content não podem ser vazios."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
