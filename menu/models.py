from django.db import models

LIMIT_LENGTH: int = 20


class Menu(models.Model):
    title = models.CharField(
        max_length=LIMIT_LENGTH,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=LIMIT_LENGTH,
        verbose_name='Слаг'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(
        max_length=LIMIT_LENGTH,
        verbose_name='Название элемента'
    )
    slug = models.SlugField(
        max_length=LIMIT_LENGTH,
        verbose_name='Слаг'
    )
    menu = models.ForeignKey(
        Menu,
        blank=True,
        related_name='items',
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='childrens',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'элементы меню'

    def __str__(self):
        return self.title
