from django.shortcuts import render
from .models import *
from django.contrib import messages
from rest_framework import generics
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

def addstar(request):
    if request.method == 'POST':
        star = Rating(request.POST)
        stars = []
        stars += star
        messages.success(request, 'Вы успешно отправили отзыв', star)

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CategoryUpdateView(generics.UpdateAPIView):
    serializers_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CategoryListView(generics.ListAPIView):
    serializers_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CategoryDestroyView(generics.DestroyAPIView):
    serializers_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ActorCreateView(generics.CreateAPIView):
    serializer_class = ActorSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ActorUpdateView(generics.UpdateAPIView):
    serializers_class = ActorSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ActorGenericView(generics.GenericAPIView):
    serializers_class = ActorSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ActorListView(generics.ListAPIView):
    serializers_class = ActorSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ActorDestroyView(generics.DestroyAPIView):
    serializers_class = ActorSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieCreateView(generics.CreateAPIView):
    serializers_class = MovieSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieUpdateView(generics.UpdateAPIView):
    serializers_class = MovieSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieGenericView(generics.GenericAPIView):
    serializers_class = MovieSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieListView(generics.ListAPIView):
    serializers_class = MovieSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieDestroyView(generics.DestroyAPIView):
    serializers_class = MovieSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializers_class = GenreSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class GenreUpdateView(generics.UpdateAPIView):
    serializers_class = GenreSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class GenreGenericView(generics.GenericAPIView):
    serializers_class = GenreSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class GenreListView(generics.ListAPIView):
    serializers_class = GenreSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class GenreDestroyView(generics.DestroyAPIView):
    serializers_class = GenreSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class RatingCreateView(generics.CreateAPIView):
    serializers_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class RatingUpdateView(generics.UpdateAPIView):
    serializers_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class RatingGenericView(generics.GenericAPIView):
    serializers_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class RatingListView(generics.ListAPIView):
    serializers_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class RatingDestroyView(generics.DestroyAPIView):
    serializers_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieImageCreateView(generics.CreateAPIView):
    serializers_class = MovieImageSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieImageUpdateView(generics.UpdateAPIView):
    serializers_class = MovieImageSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieImageGenericView(generics.GenericAPIView):
    serializers_class = MovieImageSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieImageListView(generics.ListAPIView):
    serializers_class = MovieImageSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MovieImageDestroyView(generics.DestroyAPIView):
    serializers_class = MovieImageSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ReviewCreateView(generics.CreateAPIView):
    serializers_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ReviewUpdateView(generics.UpdateAPIView):
    serializers_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ReviewGenericView(generics.GenericAPIView):
    serializers_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ReviewListView(generics.ListAPIView):
    serializers_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ReviewDestroyView(generics.DestroyAPIView):
    serializers_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)



