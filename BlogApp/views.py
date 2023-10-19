from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post, Like, Comment, Category
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    PostSerializer,
    CommentSerializer,
    LikeSerializer,
    CategorySerializer,
)
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


# Utilitários
def filter_posts(search_query, category_filter, author_username):
    posts = Post.objects.prefetch_related("comments", "likes")
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query)
            | Q(content__icontains=search_query)
        )
    if category_filter:
        posts = posts.filter(categories__id=category_filter)
    if author_username:
        posts = posts.filter(author__username=author_username)
    return posts.all()


# Views
@api_view(["GET"])
@permission_classes([AllowAny])
def homepage(request):
    search_query = request.GET.get("search", "")
    category_filter = request.GET.get("category", "")
    author_username = request.GET.get("author__username", "")

    posts = filter_posts(search_query, category_filter, author_username)
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)  # Utilizando o serializador aqui
        return Response(serializer.data)  # Retornando os dados serializados
    except Post.DoesNotExist:
        return Response(
            {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_post(request):
    print("Usuário autenticado: ", request.user)  # Adicione esta linha
    try:
        serializer = PostSerializer(
            data=request.data
        )  # Utilizando o serializador aqui
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return Response(
            {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_comment(request, post_id):
    print(
        "Dentro do método create_comment"
    )  # Verifique se esta linha aparece no console
    try:
        post = Post.objects.get(id=post_id)
        print("Post encontrado:", post)  # Verifique se o post é encontrado
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(
            "Erros do serializer:", serializer.errors
        )  # Imprima os erros se o serializer não for válido
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Post.DoesNotExist:
        print(
            "Post não encontrado"
        )  # Esta linha deve aparecer se o post não for encontrado
        return Response(
            {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_like(request, post_id):
    print(
        "Dentro do método create_like"
    )  # Verifique se esta linha aparece no console
    try:
        post = Post.objects.get(id=post_id)
        print("Post encontrado:", post)  # Verifique se o post é encontrado
        Like.objects.create(user=request.user, post=post)
        return Response(
            {"message": "Liked successfully"}, status=status.HTTP_201_CREATED
        )
    except Post.DoesNotExist:
        print(
            "Post não encontrado"
        )  # Esta linha deve aparecer se o post não for encontrado
        return Response(
            {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Post.DoesNotExist:
        return Response(
            {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"message": "Post deleted"}, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response(
            {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def list_comments(request, post_id):
    comments = Comment.objects.filter(post=post_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return Response(
            {"message": "Comment deleted"}, status=status.HTTP_200_OK
        )
    except Comment.DoesNotExist:
        return Response(
            {"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def list_likes(request, post_id):
    likes = Like.objects.filter(post=post_id)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_like(request, like_id):
    try:
        like = Like.objects.get(id=like_id)
        like.delete()
        return Response({"message": "Like deleted"}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response(
            {"error": "Like not found"}, status=status.HTTP_404_NOT_FOUND
        )
