from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Modelo para Categoria do Post."""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Modelo para um Post de Blog."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(Category, related_name="posts")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    """Modelo para um Like de Post."""

    user = models.ForeignKey(
        User, related_name="likes", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name="likes", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.post.title}"


class Comment(models.Model):
    """Modelo para Comentários."""

    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
