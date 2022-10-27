from django.db import models

class Site(models.Model):
    caption = models.CharField(verbose_name="Название", max_length=50, unique=True)
    title = models.CharField(verbose_name="Заголовок", max_length=100, blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    domain = models.CharField(verbose_name="Доменное имя", max_length=100, default="www.mysite.com")

    class Meta:
        verbose_name = "Сайт"
        verbose_name_plural = "Сайты"

    def __str__(self):
        return self.caption

class IslandType(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.caption

class Island(models.Model):
    identity = models.CharField(verbose_name="Идентификатор", max_length=50, unique=True, default="item_000")
    caption = models.CharField(verbose_name="Наименование", max_length=100)
    type = models.ForeignKey(IslandType, verbose_name="Тип компоненты", on_delete=models.SET_NULL, null=True)
    text = models.TextField(verbose_name="Текст", null=True, blank=True)
    callback = models.CharField(verbose_name="Отклик", max_length=50, null=True)

    class Meta:
        verbose_name = "Компонента"
        verbose_name_plural = "Компоненты"

    def __str__(self):
        return self.caption

class Item(models.Model):
    identity = models.CharField(verbose_name="Идентификатор", max_length=50, unique=True, default="item_000")
    caption = models.CharField(verbose_name="Наименование", max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    site = models.ForeignKey(Site, verbose_name="Сайт", on_delete=models.SET_NULL, null=True)
    islands = models.ManyToManyField(Island, verbose_name="Компоненты")

    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"

    def __str__(self):
        return self.caption

class TestModel(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50)
    description = models.TextField(verbose_name="Описание", null=True)

    def __str__(self):
        return self.caption