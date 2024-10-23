from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import LENGTH_TEXT

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='название'
    )
    slug = models.SlugField(max_length=50,)
    description = models.TextField(verbose_name='описание')

    class Meta:
        default_related_name = 'group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='текст')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='изображение'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='группа'
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='пост'
    )
    text = models.TextField(verbose_name='текст')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (
            f'{self.text[:LENGTH_TEXT]}'
            f'Автор: {self.author.username}'
            f'Пост: {self.post.id}'
        )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='Пользователь'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='подписки'
    )

    class Meta:
        unique_together = ('name', 'owner')
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return (
            f'Пользователь: {self.user.username}'
            f'Подписка: {self.following.username}'
        )
