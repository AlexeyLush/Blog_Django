from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


import string


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='опубликовано')


class Post(models.Model):
    STATUS_CHOICE = (
        ('черновик', 'Черновик'),
        ('опубликовано', 'Опубликовано')
    )
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name="Заголовок(лат)")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Автор")
    body = models.TextField(verbose_name="Текст")
    image = models.ImageField(verbose_name="Изображение", default='/static/images/default_image.png',
                              upload_to="blog/static/images")
    viewsUser = models.IntegerField(default=0, editable=False)
    sharesUser = models.IntegerField(default=0, editable=False)
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дато обновления")
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='draft', verbose_name="Статус")
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def get_img_url(self):
        return self.image.name.replace('blog', '')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    body = models.TextField(verbose_name="Комментарий")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дато обновления")
    active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

