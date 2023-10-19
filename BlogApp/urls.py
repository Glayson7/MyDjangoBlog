from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("create/", views.create_post, name="create_post"),
    path(
        "comment/<int:post_id>/", views.create_comment, name="create_comment"
    ),
    path("like/<int:post_id>/", views.create_like, name="create_like"),
    path("categories/", views.list_categories, name="list_categories"),
    path("update_post/<int:post_id>/", views.update_post, name="update_post"),
    path("delete_post/<int:post_id>/", views.delete_post, name="delete_post"),
    path(
        "list_comments/<int:post_id>/",
        views.list_comments,
        name="list_comments",
    ),
    path(
        "delete_comment/<int:comment_id>/",
        views.delete_comment,
        name="delete_comment",
    ),
    path("list_likes/<int:post_id>/", views.list_likes, name="list_likes"),
    path("delete_like/<int:like_id>/", views.delete_like, name="delete_like"),
]
