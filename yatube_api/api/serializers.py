from rest_framework import serializers

from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group.

    Поля:
    - id: ID группы (целое число).
    - title: Название группы (строка).
    - slug: Уникальный идентификатор группы (строка).
    - description: Описание группы (строка).
    """

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post.

    Поля:
    - id: ID поста (целое число).
    - text: Текст поста (строка).
    - author: Автор поста (только для чтения, строка - имя пользователя).
    - image: Изображение поста (строка - URL изображения).
    - group: Группа, к которой относится пост (целое число - ID группы).
    - pub_date: Дата публикации поста (дата и время).
    """

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment.

    Поля:
    - id: ID комментария (целое число).
    - author: Автор комментария (только для чтения, строка - имя пользователя).
    - post: Пост, к которому относится комментарий (целое число - ID поста).
    - text: Текст комментария (строка).
    - created: Дата создания комментария (дата и время).
    """

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
