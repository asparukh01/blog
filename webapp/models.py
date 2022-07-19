from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db.models.deletion import get_candidate_relations_to_delete


class Manager(models.Manager):
    def get_queryset(self):
        return super(Manager, self).get_queryset().filter(is_deleted=False)


class IsDeletedMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = Manager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        delete_candidates = get_candidate_relations_to_delete(self.__class__._meta)
        if delete_candidates:
            for rel in delete_candidates:
                if rel.on_delete.__name__ == 'CASCADE' and rel.one_to_many and not rel.hidden:
                    for item in getattr(self, rel.related_name).all():
                        item.delete()

        self.save(update_fields=['is_deleted', ])

    class Meta:
        abstract = True


class Post(IsDeletedMixin):
    STATUSES = [
        ('Не опубликован', 'Не опубликован'),
        ('Опубликован', 'Опубликован')
    ]
    title = models.CharField(max_length=150, verbose_name='Название')
    link = models.CharField(max_length=300, null=True, blank=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='post_pics', verbose_name='Image')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст поста')
    category = models.ForeignKey(to='webapp.Category', on_delete=models.CASCADE,
                                 verbose_name='Категория', related_name='posts', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=50, choices=STATUSES, default='Не опубликован', verbose_name='Статус')
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                 verbose_name='Рейтинг', default=0)
    author = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='Автор', related_name='posts'
    )
    publicated_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title


class Comment(IsDeletedMixin):
    post = models.ForeignKey(
        to='webapp.Post', on_delete=models.CASCADE,
        related_name='comments', verbose_name='Пост'
    )
    author = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='comments'
    )
    comment_text = models.TextField(max_length=3000, verbose_name='Текст коментария')
    created_at_comment = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания коментария')

    def __str__(self):
        return self.comment_text[:20]


class Category(IsDeletedMixin):
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Категория")

    def __str__(self):
        return self.title
